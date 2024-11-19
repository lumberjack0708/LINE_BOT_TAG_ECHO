from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Line Bot 的基本設定
line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

# 全域變數，用於儲存 Bot 的顯示名稱
bot_display_name = None

# 取得 Bot 的顯示名稱
def get_bot_display_name():
    global bot_display_name
    if bot_display_name is None:
        try:
            bot_info = line_bot_api.get_bot_info()
            bot_display_name = bot_info.display_name
        except LineBotApiError as e:
            print(f"取得 Bot 顯示名稱時發生錯誤: {e}")
    return bot_display_name

# 設定 webhook 路由
@app.route("/callback", methods=['POST'])
def callback():
    # 獲取請求頭中的簽名
    signature = request.headers['X-Line-Signature']

    # 獲取請求體
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # 驗證簽名並處理請求
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 處理訊息事件
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 只處理群組訊息
    if event.source.type != 'group':
        return

    # 取得 Bot 的顯示名稱
    bot_name = get_bot_display_name()
    if not bot_name:
        return

    # 取得訊息內容
    message_text = event.message.text

    # 檢查訊息文字中是否包含 @BotName
    if f"@{bot_name}" in message_text:
        # 執行您的動作，例如回覆訊息
        reply_text = '您@我，有屁快放？'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text)
        )

# 啟動 Flask 應用程式
if __name__ == "__main__":
    app.run(port=5000)
