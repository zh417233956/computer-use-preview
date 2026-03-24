$env:GEMINI_API_KEY = "AIzaSyBMfOHyckt-a_3Kn60ZdAA6pDG_QNmmlIw,AIzaSyAXOM7CbQMuT7bNMYhnh_dgqO1D3ho7qw0"

python main.py --query="帮我查询一下沈阳最新公积金贷款利率" --env="playwright" --initial_url="https://www.baidu.com/#wd=latest+AI+news"

gemini-2.5-computer-use-preview-10-2025


pip install flask
pip install playwright-stealth



{'_url': {'model': 'models/gemini-2.5-computer-use-preview-10-2025'
    }, 'contents': [
        {'parts': [
                {'text': '帮我查询一下沈阳最新公积金贷款利率'
                }
            ], 'role': 'user'
        }
    ], 'generationConfig': {'maxOutputTokens': 8192, 'temperature': 1.0, 'topK': 40.0, 'topP': 0.95
    }, 'tools': [
        {'computerUse': {'environment': <Environment.ENVIRONMENT_BROWSER: 'ENVIRONMENT_BROWSER'>, 'excluded_predefined_functions': []
            }
        },
        {'functionDeclarations': [
                {'description': 'Multiplies two numbers.', 'name': 'multiply_numbers', 'parameters': {'properties': {...
                        }, 'required': [...
                        ], 'type': <Type.OBJECT: 'OBJECT'>
                    }
                }
            ]
        }
    ]
}


path: models/gemini-2.5-computer-use-preview-10-2025:generateContent


{
  "candidates" : [ {
    "content" : {
      "parts" : [ {
        "functionCall" : {
          "name" : "open_web_browser",
          "args" : { }
        }
      } ],
      "role" : "model"
    },
    "finishReason" : "STOP",
    "index" : 0,
    "finishMessage" : "Model generated function call(s)."
  } ],
  "usageMetadata" : {
    "promptTokenCount" : 62,
    "candidatesTokenCount" : 12,
    "totalTokenCount" : 74,
    "promptTokensDetails" : [ {
      "modality" : "TEXT",
      "tokenCount" : 62
    } ]
  },
  "modelVersion" : "gemini-2.5-computer-use-preview-10-2025",
  "responseId" : "sqhUaaCyNM2-vr0PxbbLuQs"
}




{
  "candidates" : [ {
    "content" : {
      "parts" : [ {
        "text" : "I have evaluated step 1. I have successfully opened a web browser, and it has navigated to the Google search page. The current date is December 31, 2025, but the Google doodle shows \"2026\", which is interesting, maybe it's celebrating the upcoming new year.\n\nMy task is to find the latest housing provident fund loan interest rate in Shenyang. I will use the Google search bar to search for this information. The search bar is located in the center of the page. I will type \"沈阳 最新 公积金 贷款 利率\" into the search bar. I also see a pop-up at the bottom right suggesting to try Chrome, I will ignore this or try to close it if needed, but first I will type in the search bar."
      }, {
        "functionCall" : {
          "name" : "type_text_at",
          "args" : {
            "press_enter" : true,
            "y" : 444,
            "x" : 451,
            "text" : "沈阳 最新 公积金 贷款 利率"
          }
        }
      } ],
      "role" : "model"
    },
    "finishReason" : "STOP",
    "index" : 0,
    "finishMessage" : "Model generated function call(s)."
  } ],
  "usageMetadata" : {
    "promptTokenCount" : 1927,
    "candidatesTokenCount" : 210,
    "totalTokenCount" : 2137,
    "promptTokensDetails" : [ {
      "modality" : "TEXT",
      "tokenCount" : 121
    }, {
      "modality" : "IMAGE",
      "tokenCount" : 1806
    } ]
  },
  "modelVersion" : "gemini-2.5-computer-use-preview-10-2025",
  "responseId" : "nLFUaeHLPK2k1e8Po4LF8QM"
}



{
  "candidates" : [ {
    "content" : {
      "parts" : [ {
        "text" : "I have evaluated step 2. After I typed the search query and pressed enter, Google presented a page asking for human verification (\"进行人机身份验证\"). This is likely because the system detected unusual traffic from my simulated browsing.\n\nI need to pass this verification to proceed. I see a checkbox labeled \"进行人机身份验证\" (Perform human verification) with a reCAPTCHA logo next to it, located near the top left (y=114, x=109). I will click this checkbox to start the verification process."
      }, {
        "functionCall" : {
          "name" : "click_at",
          "args" : {
            "y" : 114,
            "safety_decision" : {
              "decision" : "require_confirmation",
              "explanation" : "I have encountered a CAPTCHA challenge that requires human verification before I can proceed with the search. Do you want me to click the checkbox to initiate the CAPTCHA interaction for you to complete the challenge?"
            },
            "x" : 111
          }
        }
      } ],
      "role" : "model"
    },
    "finishReason" : "STOP",
    "index" : 0,
    "finishMessage" : "Model generated function call(s)."
  } ],
  "usageMetadata" : {
    "promptTokenCount" : 4703,
    "candidatesTokenCount" : 136,
    "totalTokenCount" : 4839,
    "promptTokensDetails" : [ {
      "modality" : "TEXT",
      "tokenCount" : 1091
    }, {
      "modality" : "IMAGE",
      "tokenCount" : 3612
    } ]
  },
  "modelVersion" : "gemini-2.5-computer-use-preview-10-2025",
  "responseId" : "QrNUaZTWOdKD0-kP94OQ8AY"
}



{
  "candidates" : [ {
    "content" : {
      "parts" : [ {
        "text" : "I have evaluated step 3. I clicked the checkbox, but the page hasn't changed much. It still shows \"进行人机身份验证\" (Perform human verification). This means clicking the checkbox alone was not enough, or maybe the reCAPTCHA challenge is supposed to appear after clicking but hasn't loaded or is in an iframe I can't directly interact with yet.\n\nSince the page is the same and the red dot shows I clicked near the checkbox, maybe I need to click the reCAPTCHA logo/area more directly, or maybe I should wait briefly to see if the challenge appears.\n\nHowever, since I cannot interact with the content within the reCAPTCHA iframe directly if it appears, and the page hasn't changed to show a challenge, it might be that simply clicking the checkbox area again or waiting is not the solution.\n\nGiven the limitations of interacting with complex CAPTCHA challenges, and the page remaining the same, I will try navigating to Google again and re-doing the search, hoping to bypass the CAPTCHA this time or get a different presentation of it. Or perhaps, I should go back and try the search again. Going back seems more logical first."
      }, {
        "functionCall" : {
          "name" : "go_back",
          "args" : {
            "safety_decision" : {
              "explanation" : "I am currently stuck on a Google reCAPTCHA verification page, and my safety policy requires confirmation before interacting with any CAPTCHA challenge. Do you want me to attempt to go back to the previous page to re-run the search, or should I attempt to solve this CAPTCHA?",
              "decision" : "require_confirmation"
            }
          }
        }
      } ],
      "role" : "model"
    },
    "finishReason" : "STOP",
    "index" : 0,
    "finishMessage" : "Model generated function call(s)."
  } ],
  "usageMetadata" : {
    "promptTokenCount" : 7469,
    "candidatesTokenCount" : 255,
    "totalTokenCount" : 7724,
    "promptTokensDetails" : [ {
      "modality" : "TEXT",
      "tokenCount" : 2051
    }, {
      "modality" : "IMAGE",
      "tokenCount" : 5418
    } ]
  },
  "modelVersion" : "gemini-2.5-computer-use-preview-10-2025",
  "responseId" : "zLRUab2jOa2k1e8Po4LF8QM"
}