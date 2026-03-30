<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>關山親水公園導覽</title>
    <style>
        :root {
            --primary-color: #2E8B57; /* 海洋綠，符合自然主題 */
            --bg-color: #F4F7F6;
            --card-bg: #FFFFFF;
            --text-main: #333333;
            --text-sub: #666666;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: var(--bg-color);
            margin: 0;
            padding: 0;
            color: var(--text-main);
            display: flex;
            justify-content: center;
        }

        /* 模擬手機螢幕寬度 */
        .app-container {
            width: 100%;
            max-width: 414px; 
            background-color: var(--bg-color);
            min-height: 100vh;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
            padding-bottom: 30px;
        }

        /* 頂部橫幅 */
        .header-image {
            width: 100%;
            height: 220px;
            background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%);
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
        }

        .title-section {
            padding: 0 20px;
            margin-bottom: 20px;
        }

        .title-section h1 {
            margin: 0;
            font-size: 26px;
            color: var(--primary-color);
        }

        /* 資訊卡片清單 */
        .info-list {
            padding: 0 20px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .card {
            background-color: var(--card-bg);
            border-radius: 12px;
            padding: 16px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .card-header {
            display: flex;
            align-items: center;
            font-weight: bold;
            font-size: 16px;
            color: var(--primary-color);
        }

        .icon {
            margin-right: 8px;
            font-size: 18px;
        }

        .card-content {
            font-size: 15px;
            line-height: 1.5;
            color: var(--text-sub);
        }

        .highlight-box {
            background-color: #E8F5E9;
            padding: 10px;
            border-radius: 8px;
            margin-top: 5px;
            font-size: 14px;
        }
        
        .highlight-box strong {
            color: var(--primary-color);
        }
    </style>
</head>
<body>

    <div class="app-container">
        <div class="header-image">
            關山親水公園
        </div>

        <div class="title-section">
            <h1>園區導覽資訊</h1>
        </div>

        <div class="info-list">
            
            <div class="card">
                <div class="card-header"><span class="icon">📍</span>地址</div>
                <div class="card-content">台東縣關山鎮隆盛路 1 號</div>
            </div>

            <div class="card">
                <div class="card-header"><span class="icon">⏰</span>開放時間</div>
                <div class="card-content">每日 07:00 – 17:30<br><small>（實際開放時間依現場公告為準）</small></div>
            </div>

            <div class="card">
                <div class="card-header"><span class="icon">🎫</span>門票</div>
                <div class="card-content" style="color: #E53935; font-weight: bold;">
                    免費入園<br><small style="color: var(--text-sub); font-weight: normal;">（自 2026/3/30 年起已全面取消收費）</small>
                </div>
            </div>

            <div class="card">
                <div class="card-header"><span class="icon">🚗</span>交通方式</div>
                <div class="card-content">
                    <div class="highlight-box">
                        <strong>🚆 大眾運輸：</strong><br>
                        搭乘火車至「關山車站」，出站後步行約 1.2 公里，或於車站附近直接租借自行車/電動車前往。
                    </div>
                    <div class="highlight-box">
                        <strong>🚙 自行開車：</strong><br>
                        台九線約 333.2K 處東側轉入，園區設有免費停車場。
                    </div>
                </div>
            </div>

            <div class="card">
                <div class="card-header"><span class="icon">⏳</span>建議停留</div>
                <div class="card-content">1.5 至 2 小時<br><small>（若結合環鎮自行車道騎乘，建議安排半天行程）</small></div>
            </div>

        </div>
    </div>

</body>
</html>
