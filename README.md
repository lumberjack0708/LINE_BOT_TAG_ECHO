# Flask Tag Echo Line Bot 

這是一個使用 Flask 建立的 Line Bot 範例，並且能夠回應特定的群組訊息。

## 需求

1. Python 3.x
2. pip
3. Line Developer 帳號 (需設定 Channel Access Token 和 Channel Secret)
4. 安裝以下 Python 套件：
    - Flask
    - python-dotenv
    - line-bot-sdk

## 安裝與設定

### 1. 安裝相依套件

在專案的目錄下，開啟終端機，並輸入以下命令來安裝必要的 Python 套件：

```sh
pip install flask python-dotenv line-bot-sdk
```

### 2. 建立環境變數文件 (.env)

在專案根目錄下創建一個 `.env` 文件，並加入您的 Line Channel Access Token 和 Channel Secret：

```
LINE_CHANNEL_ACCESS_TOKEN=你的ChannelAccessToken
LINE_CHANNEL_SECRET=你的ChannelSecret
```

### 3. 執行 Flask 應用程式

在終端機中輸入以下命令來啟動 Flask 應用程式：

```sh
python app.py
```

Flask 會在預設的 5000 埠啟動 Web 伺服器，你可以使用 ngrok 來將本地的 5000 埠暴露到外網，讓 Line Bot 可以接收到來自 Line 平台的事件。

```sh
ngrok http 5000
```

將 ngrok 產生的 URL（例如 `https://abcd1234.ngrok.io`）設定為 Line 的 Webhook URL。

## 使用方式

這隻 Line Bot 主要功能如下：

1. 只回應群組中的訊息
2. 當訊息中包含 `@BotName` 的字樣時，會回應特定的訊息

`@BotName` 會自動被替換成您的 Bot 的顯示名稱。

### Line Bot 群組回應

當 Bot 被群組中的某人 `@` 時，Bot 會回應：「您@我，有屁快放？」。

## 程式碼結構

- `app.py`: 主程式，包含 Flask 的啟動與 Line Bot 的事件處理。

## 注意事項

1. 本範例僅支援群組訊息。
2. 請確保 `.env` 中的 Channel Access Token 和 Channel Secret 設定正確。
3. 請務必保護好您的 Token 和 Secret，避免外洩。

## 參考

- [Line Bot SDK for Python GitHub](https://github.com/line/line-bot-sdk-python)
- [ngrok 官方網站](https://ngrok.com/)
