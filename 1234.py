import streamlit as st
import streamlit.components.v1 as components

# 設定 Streamlit 頁面配置
st.set_page_config(page_title="關山親水公園導覽", layout="centered")

# 將 HTML、CSS 與圖片整合
# 這裡使用您生成的四張獨立圖片網址
app_html = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        :root {
            --primary: #2E8B57;
            --bg: #F4F7F6;
            --card-bg: #FFFFFF;
        }
        
        body {
            font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto;
            background-color: var(--bg);
            margin: 0;
            display: flex;
            justify-content: center;
        }

        .app-container {
            width: 100%;
            max-width: 414px;
            background-color: var(--bg);
            min-height: 100vh;
            padding-bottom: 30px;
        }

        .header {
            background: linear-gradient(135deg, #74ebd5, #2E8B57);
            color: white;
            padding: 30px 20px;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            border-bottom-left-radius: 20px;
            border-bottom-right-radius: 20px;
        }

        .section-title {
            padding: 20px 20px 10px;
            font-size: 18px;
            color: var(--primary);
            font-weight: bold;
        }

        /* 圖片網格佈局 */
        .image-grid {
            display: grid;
            grid-template-columns: 1fr 1fr; /* 兩欄 */
            gap: 12px;
            padding: 0 20px;
        }

        .image-card {
            background: var(--card-bg);
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        .image-card img {
            width: 100%;
            height: 120px;
            object-fit: cover; /* 確保圖片填滿格線且不變形 */
            display: block;
        }

        .image-caption {
            padding: 6px;
            font-size: 12px;
            text-align: center;
            color: #555;
            background: #fff;
        }

        .info-card {
            margin: 15px 20px;
            padding: 15px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }

        .info-item {
            margin-bottom: 8px;
            font-size: 14px;
            line-height: 1.5;
        }

        .label {
            font-weight: bold;
            color: var(--primary);
        }
    </style>
</head>
<body>

    <div class="app-container">
        <div class="header">關山親水公園導覽</div>

        <div class="section-title">🌿 公園美景</div>
        <div class="image-grid">
            <div class="image-card">
                <img src="http://googleusercontent.com/image_generation_content/3" alt="景點1">
                <div class="image-caption">湖畔倒影</div>
            </div>
            <div class="image-card">
                <img src="http://googleusercontent.com/image_generation_content/4" alt="景點2">
                <div class="image-caption">景觀吊橋</div>
            </div>
            <div class="image-card">
                <img src="http://googleusercontent.com/image_generation_content/5" alt="景點3">
                <div class="image-caption">環鎮單車道</div>
            </div>
            <div class="image-card">
                <img src="http://googleusercontent.com/image_generation_content/6" alt="景點4">
                <div class="image-caption">生態池景</div>
            </div>
        </div>

        <div class="section-title">📍 基本資訊</div>
        <div class="info-card">
            <div class="info-item"><span class="label">地址：</span>台東縣關山鎮隆盛路 1 號</div>
            <div class="info-item"><span class="label">開放：</span>每日 07:00 – 17:30</div>
            <div class="info-item"><span class="label">門票：</span><span style="color:red; font-weight:bold;">免費入園</span></div>
            <div class="info-item"><span class="label">建議：</span>結合 12 公里環鎮自行車道遊玩</div>
        </div>
    </div>

</body>
</html>
"""

# 使用 Streamlit 渲染
components.html(app_html, height=800, scrolling=True)
