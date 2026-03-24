from flask import Flask, request, jsonify
from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth
import threading
import time


class DouBaoAPI:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, user_data_path=r"E:\playwright_data"):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.user_data_path = user_data_path
                cls._instance.browser_started = False
        return cls._instance

    def _ensure_browser(self):
        """确保浏览器在当前环境下已启动"""
        if not self.browser_started:
            # 启动同步 Playwright
            self.pw = sync_playwright().start()

            # 配置建议：添加更多规避参数
            self.context = self.pw.chromium.launch_persistent_context(
                user_data_dir=self.user_data_path,
                headless=False,
                # 关键：排除掉会让 Chrome 显示提示条的开关
                # '--no-sandbox',
                ignore_default_args=["--enable-automation"],
                args=[
                    '--start-maximized',
                    '--disable-blink-features=AutomationControlled',  # 禁用自动化控制特征
                    '--disable-infobars',  # 禁用“受自动化软件控制”的提示条
                    # '--ignore-certificate-errors',
                    # '--log-level=3',  # 减少日志输出
                ],
                no_viewport=True,
                # 建议固定一个 User-Agent，避免使用带有 Headless 字样的默认值
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )

            # 获取默认页面
            self.page = self.context.pages[0]

            # --- 使用 stealth 改造开始 ---
            # 1. 应用 playwright-stealth 的标准全套伪装
            # stealth(self.page)

            # --- 改造部分 ---
            stealth_config = Stealth()
            # 注意：这里调用的是 apply_stealth 方法
            stealth_config.apply_stealth_sync(self.page)
            # ----------------

            # 2. 额外手动补丁 (针对一些最新的检测手段)
            self.page.add_init_script("""
                // 抹除 webdriver 特征
                Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
                // 伪造语言和平台
                Object.defineProperty(navigator, 'languages', {get: () => ['zh-CN', 'zh']});
                Object.defineProperty(navigator, 'platform', {get: () => 'Win32'});
            """)
            # --- 使用 stealth 改造结束 ---

            self.page.goto("https://www.doubao.com")
            self.browser_started = True
            time.sleep(2)

    def _ensure_browser_old(self):
        """确保浏览器在当前环境下已启动"""
        if not self.browser_started:
            # 注意：在线程中启动同步 Playwright
            self.pw = sync_playwright().start()
            self.context = self.pw.chromium.launch_persistent_context(
                user_data_dir=self.user_data_path,
                headless=False,
                args=['--start-maximized'],
                no_viewport=True
            )
            self.page = self.context.pages[0]

            # 帮我使用stealth改造
            stealth_config = Stealth()
            # 注意：这里调用的是 apply_stealth 方法
            stealth_config.apply_stealth_sync(self.page)

            self.page.goto("https://www.doubao.com")
            self.browser_started = True
            time.sleep(2)

    def send_message(self, text, timeout=30):
        # 使用锁确保同一时间只有一个线程在操作浏览器，防止 greenlet 切换错误
        with self._lock:
            self._ensure_browser()

            try:
                # 检查页面是否意外关闭
                if self.page.is_closed():
                    self.page = self.context.new_page()
                    self.page.goto("https://www.doubao.com")

                # 定位输入框
                input_xpath = "xpath=//textarea[@data-testid='chat_input_input']"
                self.page.wait_for_selector(input_xpath, timeout=10000)

                # 输入并发送
                self.page.fill(input_xpath, text)
                self.page.keyboard.press("Enter")

                # 循环监测结果
                start_time = time.time()
                regen_xpath = "xpath=//*[@data-testid='message_action_regenerate']"
                content_xpath = "xpath=//*[@data-testid='message_text_content']"

                while time.time() - start_time < timeout:
                    # 获取“重新生成”按钮作为结束标志
                    regen_btn = self.page.locator(regen_xpath).last
                    if regen_btn.is_visible():
                        # 提取文本
                        result = self.page.locator(content_xpath).last.inner_text()
                        return result
                    time.sleep(1)

                return None
            except Exception as e:
                print(f"操作异常: {e}")
                raise e


app = Flask(__name__)
api = DouBaoAPI()


@app.route("/send", methods=["POST"])
def send():
    data = request.json
    text = data.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        # 这里的调用会进入 API 的锁机制
        result = api.send_message(text)
        if result:
            return jsonify({"result": result})
        return jsonify({"error": "Wait timeout"}), 504
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # 关键点 1：关闭 debug 模式
    # 关键点 2：如果并发量大，建议 threaded=False，但会导致请求排队
    # 这里保持 threaded=True，靠 api._lock 来解决 greenlet 冲突
    app.run(host="0.0.0.0", port=8800,  debug=False, threaded=False)