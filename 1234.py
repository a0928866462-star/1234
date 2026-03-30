import streamlit as st
import streamlit.components.v1 as components

# 設定 Streamlit 網頁標題
st.set_page_config(page_title="關山親水公園導覽", layout="centered")

# 定義圖片連結與名稱
images = [
    {"name": "湖畔晨曦倒影", "url": "https://lh3.googleusercontent.com/d/1X5X8_B1X5X8_B1X5X8_B1X5X8_B1X5X8"},
    {"name": "縱谷景觀吊橋", "url": "https://lh3.googleusercontent.com/d/1Y6Y9_B2Y6Y9_B2Y6Y9_B2Y6Y9_B2Y6Y9"},
    {"name": "環鎮自行車道", "url": "https://lh3.googleusercontent.com/d/1Z7Z0_B3Z7Z0_B3Z7Z0_B3Z7Z0_B3Z7Z0"},
    {"name": "生態濕地木棧道", "url": "https://lh3.googleusercontent.com/d/1A8A1_B4A8A1_B4A8A1_B4A8A1_B4A8A1"}
]

# 將 HTML 與 CSS 包裝成字串
app_html = f"""
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>關山親水公園導覽</title>
    <style>
        :root {{
            --primary-color: #2E8B57;
            --bg-color: #F4F7F6;
            --card-bg: #FFFFFF;
            --text-main: #333333;
            --text-sub: #666666;
            --accent-color: #4A90E2;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: var(--bg-color);
            margin: 0;
            padding: 0;
            color: var(--text-main);
            display: flex;
            justify-content: center;
        }}

        .app-container {{
            width: 100%;
            max-width: 414px; 
            background-color: var(--bg-color);
            min-height: 100vh;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
            padding-bottom: 40px;
        }}

        .header-image {{
            width: 100%;
            height: 200px;
            background: linear-gradient(135deg, #74ebd5 0%, #2E8B57 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 24px;
            font-weight: bold;
            text-shadow: 1px 1px 4px rgba(0,0,0,0.3);
            border-bottom-left-radius: 20px;
            border-bottom-right-radius: 20px;
            margin-bottom: 20px;
        }}

        .section-title {{
            padding: 0 20px;
            margin: 20px 0 10px 0;
            font-size: 20px;
            color: var(--primary-color);
            border-left: 5px solid var(--primary-color);
            margin-left: 20px;
        }}

        .info-list {{
            padding: 0 20px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}

        .card {{
            background-color: var(--card-bg);
            border-radius: 12px;
            padding: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }}

        .card-header {{
            font-weight: bold;
            font-size: 15px;
            color: var(--primary-color);
            margin-bottom: 5px;
        }}

        .card-content {{
            font-size: 14px;
            color: var(--text-sub);
            line-height: 1.4;
        }}

        /* 圖片連結樣式 */
        .image-link-container {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            padding: 0 20px;
        }}

        .img-btn {{
            display: block;
            background-color: var(--accent-color);
            color: white;
            text-decoration: none;
            text-align: center;
            padding: 12px 5px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 500;
            transition: opacity 0.2s;
        }}

        .img-btn:active {{
            opacity: 0.7;
        }}

    </style>
</head>
<body>

    <div class="app-container">
        <div class="header-image">關山親水公園</div>

        <div class="section-title">實景導覽</div>
        <div class="image-link-container">
            <a href="https://r.jina.ai/i/52c678536a04473887c2b5302636220d" target="_blank" class="img-btn">🖼️ 湖畔晨曦倒影</a>
            <a href="https://r.jina.ai/i/52c678536a04473887c2b5302636220d" target="_blank" class="img-btn">🖼️ 縱谷景觀吊橋</a>
            <a href="https://r.jina.ai/i/52c678536a04473887c2b5302636220d" target="_blank" class="img-btn">🖼️ 環鎮自行車道</a>
            <a href="https://r.jina.ai/i/52c678536a04473887c2b5302636220d" target="_blank" class="img-btn">🖼️ 生態濕地木道</a>
        </div>

        <div class="section-title">園區資訊</div>
        <div class="info-list">
            <div class="card">
                <div class="card-header">📍 地址</div>
                <div class="card-content">台東縣關山鎮隆盛路 1 號</div>
            </div>
            <div class="card">
                <div class="card-header">⏰ 開放時間</div>
                <div class="card-content">每日 07:00 – 17:30</div>
            </div>
            <div class="card">
                <div class="card-header">🎫 門票資訊</div>
                <div class="card-content" style="color: #d32f2f; font-weight: bold;">免費入園 (2026/03/30起)</div>
            </div>
            <div class="card">
                <div class="card-header">🚗 交通與停留</div>
                <div class="card-content">
                    火車至關山站步行1.2km。建議停留1.5-2小時。
                </div>
            </div>
        </div>
    </div>

</body>
</html>
"""

# 渲染組件
components.html(app_html, height=800, scrolling=True)
