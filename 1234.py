import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="關山親水公園導覽", layout="centered")

# HTML 內容
app_html = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        :root { --primary: #2E8B57; --bg: #F4F7F6; }
        body { font-family: sans-serif; background: var(--bg); margin: 0; display: flex; justify-content: center; }
        .app-container { width: 100%; max-width: 414px; background: white; min-height: 100vh; }
        .header { background: linear-gradient(135deg, #74ebd5, #2E8B57); color: white; padding: 40px 20px; text-align: center; font-size: 24px; font-weight: bold; }
        .section-title { padding: 20px; font-size: 18px; color: var(--primary); font-weight: bold; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; padding: 0 20px; }
        .img-link { background: #e3f2fd; color: #1976d2; text-decoration: none; padding: 15px 10px; border-radius: 8px; text-align: center; font-size: 14px; border: 1px solid #bbdefb; }
        .info-card { margin: 15px 20px; padding: 15px; border-radius: 10px; background: #f9f9f9; border-left: 5px solid var(--primary); }
    </style>
</head>
<body>
    <div class="app-container">
        <div class="header">關山親水公園</div>
        
        <div class="section-title">🖼️ 景點實景 (點擊查看大圖)</div>
        <div class="grid">
            <a href="http://googleusercontent.com/image_generation_content/3" target="_blank" class="img-link">靜謐湖泊區</a>
            <a href="http://googleusercontent.com/image_generation_content/4" target="_blank" class="img-link">景觀吊橋</a>
            <a href="http://googleusercontent.com/image_generation_content/5" target="_blank" class="img-link">環鎮自行車道</a>
            <a href="http://googleusercontent.com/image_generation_content/6" target="_blank" class="img-link">生態蓮花池</a>
        </div>

        <div class="section-title">📍 遊客資訊</div>
        <div class="info-card">
            <strong>地址：</strong>台東縣關山鎮隆盛路 1 號<br>
            <strong>門票：</strong>免費入園 (2026/03/30起)<br>
            <strong>時間：</strong>07:00 – 17:30
        </div>
    </div>
</body>
</html>
"""

components.html(app_html, height=700)
