from flask import Flask, request, jsonify
from DrissionPage import Chromium, ChromiumOptions
from DrissionPage.common import Keys
import threading
import time


# 单例浏览器封装
class DouBaoAPI:
    total_call_count = 0  # 公共类属性：记录所有实例的总调用次数
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, user_data_path=r"E:\data1"):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._init_browser(user_data_path)
        return cls._instance

    def _init_browser(self, user_data_path):
        co = ChromiumOptions().set_user_data_path(user_data_path)
        self.browser = Chromium(addr_or_opts=co)
        self.tab = self.browser.latest_tab
        self.tab.get("https://www.doubao.com")
        time.sleep(2)

    def send_message(self, text, timeout=30):
        self.__class__.total_call_count += 1
        print(f"总调用次数: {self.__class__.total_call_count}")

        """发送消息并返回结果"""
        if self.__class__.total_call_count % 20 == 0:
            ele = self.tab.ele("@text()=新对话")
            ele.click()

        # ele = self.tab.ele('@data-testid=message_action_edit', timeout=1) #编辑按钮
        # if ele:
        #     ele.click()
        #     time.sleep(0.5)
        #     ele.click()

        #     ele = self.tab.ele("@data-testid=editing_message_content_input", timeout=1) #编辑
        #     ele.clear()
        #     ele.input(text)

        #     time.sleep(0.5)

        #     confirm = self.tab.ele('@data-testid=editing_message_content_confirm', timeout=1) #确认按钮
        #     confirm.click()
        #     time.sleep(0.5)
        #     confirm.click()
        # else:

        ele = self.tab.ele("@data-testid=chat_input_input", timeout=1)  # 首次
        ele.input(text + "\n")  # 自动回车

        if not ele:
            raise RuntimeError("未找到输入框")

        start_time = time.time()
        time.sleep(4)
        while True:
            # wrapper1 = self.tab.ele('.entry-btn-title-v3-uM2642', timeout=1) #参考N片文章 出现后 表是输出结束
            # wrapper2 = self.tab.ele('.suggest-list-item suggest-message-oSXMsU', timeout=1) #相关资料 出现后 表是输出结束
            wrapper3 = self.tab.ele("@data-testid=message_action_regenerate", timeout=1)  # 刷新按钮
            if wrapper3:
                eles = self.tab.eles("@data-testid=message_text_content")  # 获取输出内容
                if eles:
                    return eles[-1].text
            if time.time() - start_time > timeout:
                return None
            time.sleep(1)


# Flask 实例
app = Flask(__name__)

# 初始化浏览器单例
api = DouBaoAPI()


@app.route("/send", methods=["POST"])
def send():
    data = request.json
    if not data or "text" not in data:
        return jsonify({"error": "缺少 text 参数"}), 400
    text = data["text"]
    timeout = data.get("timeout", 30)
    try:
        result = api.send_message(text, timeout=timeout)
        if result is None:
            return jsonify({"error": "超时未获取结果"}), 504
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
