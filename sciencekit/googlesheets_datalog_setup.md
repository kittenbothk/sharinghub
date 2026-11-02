---
description: 適用於 Future LiteAI：由本機讀數、Wi-Fi 與 Google 授權設定，到 Google Sheets 資料記錄及網頁儀表板的完整使用教學。
---

# Google Sheets Datalogger設定教學

科學教育測量套件的未來板Lite AI現正支援將數據上傳到Google Sheets，詳細使用方法請參考以下教學。

## 1. Google Sheets API設定

首先請按照以下教學設定好Google Sheets API帳戶。

{% content-ref url="../mcu/liteai/liteai-x-google-sheets/liteaixgoogle-sheets-she-ding.md" %}
[liteaixgoogle-sheets-she-ding.md](../mcu/liteai/liteai-x-google-sheets/liteaixgoogle-sheets-she-ding.md)
{% endcontent-ref %}

## 2. 下載參考程式

{% file src="../.gitbook/assets/科學測量套件Google Sheets PY.zip" %}

本套件不包含 Google 權杖、OAuth 用戶端憑證、個人 Wi-Fi 資料、dashboard.json 或測試資料。已附九個本機顯示用 Python 程式及 soundsource.py 聲源程式；Google Sheets 記錄版本由產生器按照您的設定產生。

### 不需設定：本機讀數模式(無Datalog功能)

將zip檔內的內容複製至 Future LiteAI 根目錄，接好對應感測器，然後執行對應的 Python 程式即可查看讀數。

本機程式不會讀取 wifi.txt、token.json 或 dashboard.json，不會連接 Wi-Fi，也不會寫入記錄。無需完成 OAuth 或使用產生器。網頁儀表板是 Google Sheets 記錄模式的功能，本機顯示模式只在裝置螢幕顯示讀數。

| 程式               | 感測器／本機控制                  |
| ---------------- | ------------------------- |
| 01.Sound\_p1.py  | P1 聲音；顯示 dB               |
| 02.HPA\_i2c.py   | ENV2 氣壓；顯示 hPa            |
| 03.CO2\_i2c.py   | CO₂；按 a 重設峰值              |
| 04.PM\_i2c.py    | PMSA003I；PM2.5 及 PM10     |
| 05.Temp\_p1.py   | GPIO 4 的 DS18B20 水溫       |
| 06.NTU\_p1.py    | P1 水濁度；清水按 A 校正           |
| 07.Load\_i2c.py  | 重量；啟動時移除所有重量，按 A 歸零       |
| 08.Solar\_i2c.py | 電池電壓；沿用啟動時開啟 USB，按 A 切換輸出 |
| 09.PH\_i2c.py    | pH；試紙風格讀數顏色               |

另附 soundsource.py：持續以蜂鳴器發出 1000 Hz 聲音，可作聲音感測器測試聲源；需停止執行程式或重啟裝置以停止聲音。此程式不會記錄資料。

本機模式不使用 M 鍵開啟記錄。按 A 的控制依各感測器而定。

## 3. 準備 Google 試算表

使用已授權帳戶有編輯權限的試算表，先建立所需分頁。每個感測器可以使用不同檔案，或同一檔案的不同分頁。

儀表板讀取公開試算表，請將一般存取權設為「知道連結的任何人／檢視者」。這會讓持有連結的人讀取資料；只使用可以公開的感測器資料。裝置上載仍需 Google 授權。

<figure><img src="../.gitbook/assets/image (368).png" alt=""><figcaption></figcaption></figure>

每個程式上傳的數據格式可以參考以下表格。

| 感測器 | 第 1 列標題                |
| --- | ---------------------- |
| 聲音  | A1 時間、B1 dB            |
| 氣壓  | A1 時間、B1 hPa           |
| CO₂ | A1 時間、B1 ppm           |
| PM  | A1 時間、B1 PM2.5、C1 PM10 |
| 水溫  | A1 時間、B1 溫度（°C）        |
| 水濁度 | A1 時間、B1 NTU           |
| 重量  | A1 時間、B1 重量（g）         |
| 太陽能 | A1 時間、B1 電壓（V）         |
| pH  | A1 時間、B1 pH            |

記住要設定工作表的名稱。

<figure><img src="../.gitbook/assets/image (371).png" alt=""><figcaption></figcaption></figure>

## 4. 產生 dashboard.json 和 Python 程式

在電腦開啟 FutureLite AI上的googlesheet\_generator.html或者前往以下網址。

<figure><img src="../.gitbook/assets/image (369).png" alt=""><figcaption></figcaption></figure>

{% embed url="https://kittenbot.hk/googlesheet_generator.html" %}

#### [https://kittenbot.hk/googlesheet\_generator.html](https://kittenbot.hk/googlesheet_generator.html)

在「JSON 設定」分頁填入WiFi的登入資料。

<figure><img src="../.gitbook/assets/image (370).png" alt=""><figcaption></figcaption></figure>

### 方案A: 所有感應器共用同一個試算表

如全部感測器使用同一份試算表，可勾選共用試算表選項然後將試算表的共用連結貼上到欄位。

<figure><img src="../.gitbook/assets/image (373).png" alt=""><figcaption></figcaption></figure>

然後分別填寫工作表分頁名稱，工作表名稱對照Google Sheet上的工作表名稱。

<figure><img src="../.gitbook/assets/image (374).png" alt=""><figcaption></figcaption></figure>

### 方案B: 感應器使用不同試算表

假如感應器會使用不同試算表，就不要勾選共用試算表選項。

然後分別將試算表的連結和工作表名稱貼上到每個感應器的欄位。

<figure><img src="../.gitbook/assets/image (376).png" alt=""><figcaption></figcaption></figure>

### 下載Google Sheets版程式

按「產生全部已設定程式 ZIP」，一次下載 dashboard.json 和所有已填寫感測器的 Python 程式。解壓縮後全部放入 **裝置根目錄**，會取代對應的本機版本。

{% hint style="info" %}
* 如只需個別檔案，可按「只產生 dashboard.json」，或到個別 Python 分頁產生單一程式；設定會自動填入。各檔案同樣放入 **裝置根目錄**。ZIP 不包含 token.json 或靜態儀表板。若填寫 Wi-Fi 名稱並勾選加入 wifi.txt，ZIP 會包含該連線設定；否則保留裝置原有 wifi.txt。請保留原有 html、lib、logo 和自己的 token.json。
* 日後可匯入原有 dashboard.json，保留其他感測器的設定。修改試算表或分頁後，請重新產生並複製 JSON 和相關 Python 程式。
{% endhint %}

<figure><img src="../.gitbook/assets/image (375).png" alt=""><figcaption></figcaption></figure>

產生器只在瀏覽器本機處理資料，不會自動保存輸入；重新整理前請下載。JSON 不包含 Google 權杖或 Wi-Fi 密碼。

## 5. 覆蓋舊版測量程式

將下載的zip檔的所有檔案複製到FutureLite AI上。

<figure><img src="../.gitbook/assets/image (377).png" alt=""><figcaption></figcaption></figure>

### 裝置最終檔案結構

<figure><img src="../.gitbook/assets/image (381).png" alt=""><figcaption></figcaption></figure>

```
/dashboard.html/dashboard.json       ← 自行產生
/token.json           ← 自行授權取得
/wifi.txt             ← 填入自己的資料
/九個Python程式.py     ← 隨附本機版本；需要記錄時以產生器版本取代
/html/db.html
/html/hpa.html
/html/co2.html
/html/pm.html
/html/temp.html
/html/ntu.html
/html/load.html
/html/solar.html
/html/ph.html
/lib/（合併隨附函式庫及原有系統函式庫）
/logo/logo.png
```

## 6. 執行及查看儀表板

接妥感測器，執行該感測器的 Python 程式。

按 M 開始連線及記錄，再按 M 停止記錄。連線及首次 NTP 同步期間可能稍作等待。一般情況下，螢幕每 0.2 秒更新，雲端約每 2 秒上載。Future Lite AI會顯示裝置的IP地址及儀錶板網址。



手機或電腦連接同一本機網絡，在瀏覽器輸入裝置畫面顯示的網址：

```
http://裝置IP/dashboard.html

例:
http://192.168.8.119/dashboard.html
```

底部選單可切換九種儀表板，亦可隱藏／顯示。只會載入選中的儀表板。

<figure><img src="../.gitbook/assets/image (379).png" alt=""><figcaption></figcaption></figure>

儀表板讀取 Google 上最新 20 筆資料，每次查詢完成約 2 秒後再查詢；Google 快取可能令圖表延遲。

瀏覽器需要互聯網以載入圖表服務和試算表。

<figure><img src="../.gitbook/assets/image (380).png" alt=""><figcaption></figcaption></figure>

Google Sheets會即時更新Future Lite AI上傳的數據。

<figure><img src="../.gitbook/assets/image (378).png" alt=""><figcaption></figcaption></figure>

### 個別感測器操作

* CO₂：按 a 重設峰值。
* 水濁度：將探頭放入清水後按 A 校正，沿用原有 25°C 校正參數。
* 重量：啟動時先移除所有重量，按 A 歸零並發出確認聲。
* 太陽能：沿用啟動時 USB 輸出開啟的設定，按 A 切換輸出。

## 簡單排錯

* 畫面或圖表顯示 null／仍讀取 txt：確認已複製這套件的所有 HTML，並清除瀏覽器快取（Ctrl+F5）。
* 找不到 dashboard.json：檔案應在裝置根目錄，不能放在 html 內。
* 圖表沒有資料：檢查 JSON 的分頁名稱、公開檢視設定、第 1 列標題及感測器是否已開始上載。
* 憑證或授權錯誤：只在私人環境檢查 token.json。不要將權杖內容貼到公開討論區。
* HTTP 429：多台裝置共用同一帳戶／Cloud 專案時會共用配額，需降低頻率或規劃上載排程。
* 感測器／匯入模組錯誤：檢查接線及供應商韌體、對應的函式庫。

本機版本已做程式檢查，仍需在正式交付前逐一實機驗證；Google Sheets 版本亦需驗證所有感測器與韌體組合。本套件不包含舊資料記錄、UV 或亮度測試程式。
