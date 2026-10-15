---
hidden: true
---

# LiteAI x Google Sheets設定

## 1. Google Cloud帳號設定

首先前往Google Cloud Console建立一個Google Cloud帳戶。

[https://console.cloud.google.com/welcome/new](https://console.cloud.google.com/welcome/new)

{% embed url="https://console.cloud.google.com/welcome/new" %}

登入到您的Google 帳號，然後選擇香港地區並同意服務條款。

<figure><img src="../../../.gitbook/assets/image (327).png" alt=""><figcaption></figcaption></figure>

## 2. 建立Google Cloud項目及啟用API

### 建立Google Cloud項目

在項目挑選視窗新增專案。

<figure><img src="../../../.gitbook/assets/image (313).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (314).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (315).png" alt=""><figcaption></figcaption></figure>

### 啟用Google Sheets API

在搜尋列搜尋Google Sheets，打開Google Sheets API。

<figure><img src="../../../.gitbook/assets/image (317).png" alt=""><figcaption></figcaption></figure>

啟用Google Sheets API。

<figure><img src="../../../.gitbook/assets/image (319).png" alt=""><figcaption></figcaption></figure>

## 4. 建立Google Cloud應用程式

打開選單，在API和服務中打開OAuth同意畫面。

<figure><img src="../../../.gitbook/assets/image (321).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (323).png" alt=""><figcaption></figcaption></figure>

點擊開始，設定應用程式身份。

<figure><img src="../../../.gitbook/assets/image (324).png" alt=""><figcaption></figcaption></figure>

輸入應用程式名稱和你的Gmail電郵地址。

<figure><img src="../../../.gitbook/assets/image (328).png" alt=""><figcaption></figcaption></figure>

在目標對象裏選擇外部。

<figure><img src="../../../.gitbook/assets/image (326).png" alt=""><figcaption></figcaption></figure>

在聯絡資訊中輸入自己的Gmail電郵地址。

<figure><img src="../../../.gitbook/assets/image (329).png" alt=""><figcaption></figcaption></figure>

同意服務條款並建立程式。

<figure><img src="../../../.gitbook/assets/image (330).png" alt=""><figcaption></figcaption></figure>

## 5. 建立OAuth用戶端

打開用戶端頁面，按建立用戶端。

<figure><img src="../../../.gitbook/assets/image (331).png" alt=""><figcaption></figcaption></figure>

輸入用戶端名稱，用戶端名稱只供自己辨別所以沒有限制。

在應用程式類型中一定要選擇網頁應用程式。

<figure><img src="../../../.gitbook/assets/image (332).png" alt=""><figcaption></figcaption></figure>

在已授權的重新導向URI中輸入以下連結，然後按建立：

[https://kittenbot.hk/oauth.php](https://kittenbot.hk/oauth.php?lang=zh-Hant)

<figure><img src="../../../.gitbook/assets/image (338).png" alt=""><figcaption></figcaption></figure>

## 6. 下載用戶端憑證json檔案

<figure><img src="../../../.gitbook/assets/image (335).png" alt=""><figcaption></figcaption></figure>

## 7. 發佈Google Cloud應用程式

打開品牌頁面，輸入以下資訊。

應用程式首頁:

[https://kittenbot.hk/liteai-logger.html](https://kittenbot.hk/liteai-logger.html)

應用程式隱私權政策連結:

[https://www.privacypolicies.com/live/1bc4dc81-5b16-4d41-b8fa-71a7f982b3bf](https://www.privacypolicies.com/live/1bc4dc81-5b16-4d41-b8fa-71a7f982b3bf)

<figure><img src="../../../.gitbook/assets/image (340).png" alt=""><figcaption></figcaption></figure>

在授權網域中頁面會提示網域未獲授權，在網域輸入以下資訊再按儲存。

kittenbot.hk

privacypolicies.com

<figure><img src="../../../.gitbook/assets/image (341).png" alt=""><figcaption></figcaption></figure>

在選單中打開目標對象的頁面，然後按發布應用程式。

<figure><img src="../../../.gitbook/assets/image (342).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (343).png" alt=""><figcaption></figcaption></figure>

## 9. 取得未來板Lite AI憑證

打開以下網站：

[https://kittenbot.hk/oauth.php?lang=zh-Hant](https://kittenbot.hk/oauth.php?lang=zh-Hant)

{% embed url="https://kittenbot.hk/oauth.php?lang=zh-Hant" %}

將下載的用戶端憑證json檔案上載到網站，然後按前往Google授權。

<figure><img src="../../../.gitbook/assets/image (337).png" alt=""><figcaption></figcaption></figure>

選擇自己的Google帳號。

<figure><img src="../../../.gitbook/assets/image (339).png" alt=""><figcaption></figcaption></figure>

假如頁面提示應用程式未經驗證，請按進階，然後按 『前往kittenbot.hk』

<figure><img src="../../../.gitbook/assets/image (344).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (345).png" alt=""><figcaption></figcaption></figure>

在要求存取的頁面點擊繼續。

<figure><img src="../../../.gitbook/assets/image (346).png" alt=""><figcaption></figcaption></figure>

## 10. 下載未來板Lite的憑證檔案

頁面會顯示授權完成，請按照指示下載token.json及access\_token.txt檔案。

下載後請妥善保管檔案，在離開前請記緊清除我的設定工作階段。

<figure><img src="../../../.gitbook/assets/image (347).png" alt=""><figcaption></figcaption></figure>

