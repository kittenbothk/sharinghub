# AI鑒別器快速開始

## 程式選擇教學

未來板Lite已經預載AI鑒別器的程式，學生只須選擇相應程式即可。

{% embed url="https://youtu.be/t0IWq0CMLTk" %}

程式選擇步驟:

1. 打開電源。

<figure><img src="../../.gitbook/assets/1_1x.png" alt="" width="375"><figcaption></figcaption></figure>

2. 在介面中可以按A鍵和B鍵選擇功能，選擇右邊的運行程序，然後按M鍵確認。
3. 進入頁面後會看到所有的預載程式，使用A和B鍵選擇想啟動的程式，然後按M鍵，未來板就會啟動所選程式。

<div><figure><img src="../../.gitbook/assets/programselect1.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/programselect2.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/programselect3.png" alt=""><figcaption></figcaption></figure></div>

## 1. 模型訓練

### 下載範例圖片

[**下載範例圖片**](https://www.canva.com/design/DAGxguPrfNI/7r2qc4hzFF8wXIRoCehHXQ/view?utm_content=DAGxguPrfNI\&utm_campaign=designshare\&utm_medium=link2\&utm_source=uniquelinks\&utlId=h3cd0e17c79)

{% embed url="https://www.canva.com/design/DAGxguPrfNI/7r2qc4hzFF8wXIRoCehHXQ/view?utlId=h3cd0e17c79&utm_campaign=designshare&utm_content=DAGxguPrfNI&utm_medium=link2&utm_source=uniquelinks" %}

### 程式使用教學

打開「koi\_train.py」。

<figure><img src="../../.gitbook/assets/image (220).png" alt=""><figcaption></figcaption></figure>

1. 未來板Lite會顯示現時的標籤，例如GiantPanda，這是現時要訓練的圖像。
2. 將KOI 2對準圖片然後按A鍵，KOI 2就會錄入數據，將此圖像標籤為GiantPanda。
3. 可以在不同角度距離多錄入數張，令模型更準確。
4. 重複以上步驟直至訓練好所有該標籤的圖片。

<div><figure><img src="../../.gitbook/assets/image (222).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (223).png" alt=""><figcaption></figcaption></figure></div>

1. 按下B鍵，未來板就會跳至下一個標籤。
2. 重複以上訓練步驟，訓練所有動物圖片。

<figure><img src="../../.gitbook/assets/image (224).png" alt=""><figcaption></figcaption></figure>

完成訓練所有圖片之後，按中間的M鍵就可以將模型儲存下來。儲存成功的話KOI 2會顯示save successfully的畫面。

<figure><img src="../../.gitbook/assets/image (225).png" alt=""><figcaption></figcaption></figure>

## 2. AI鑒別器

### 程式使用教學

{% hint style="info" %}
AI鑒別器程式需要使用WiFi，請預先準備WiFi熱點。\
預設WiFi登入資料:\
SSID: hello\
Password: 12345678
{% endhint %}

打開「species\_run.py」。

未來板會自動連接到WiFi網絡。

<figure><img src="../../.gitbook/assets/image (221).png" alt=""><figcaption></figcaption></figure>

KOI 2會自動載入先前訓練的AI模型。\
按未來板的A鍵即可進行辨認。

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

未來板會顯示辨認到的動物名稱。

按未來板的B鍵，生成式AI就會生成一段文字介紹該動物並以粵語朗讀出來。

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

按下中間的M鍵，未來板就會顯示Listening。向未來板說出你的問題，未來板會將進行語音辨識。

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

生成式AI就會生成出答案並以粵語朗讀出來。

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

### 更改WiFI登入資料

如需更改WiFi的登入資料，請打開wifi.txt然後輸入新的SSID和密碼，兩者用逗號( , )分隔。

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>
