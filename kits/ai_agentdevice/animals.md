# 1. AI鑒別器中華瀕危物種上手即玩

## 程式選擇教學

未來板Lite已經預載AI鑒別器的程式，學生只須選擇相應程式即可。

{% embed url="https://youtu.be/t0IWq0CMLTk" %}

程式選擇步驟:

1. 打開電源。

<figure><img src="../../.gitbook/assets/1_1x.png" alt="" width="375"><figcaption></figcaption></figure>

2. 在介面中可以按A鍵和B鍵選擇功能，選擇右邊的運行程序，然後按M鍵確認。
3. 進入頁面後會看到所有的預載程式，使用A和B鍵選擇想啟動的程式，然後按M鍵，未來板就會啟動所選程式。

<div><figure><img src="../../.gitbook/assets/programselect1.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/programselect2.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/programselect3.png" alt=""><figcaption></figcaption></figure></div>

## 1. 中華瀕危物種AI模型訓練

打開「species\_train.py」。

<figure><img src="../../.gitbook/assets/image (289).png" alt=""><figcaption></figcaption></figure>

未來板上顯示GiantPanda，代表現在要訓練的是大熊貓的模型

把KOI 2 鏡頭對準大熊貓的圖片，按下A鍵，KOI 2 便會為大熊貓製作辨識模型數據。

試試在不同角度和距離多拍數張照片，令模型更加準確。

<figure><img src="../../.gitbook/assets/image (290).png" alt=""><figcaption></figcaption></figure>

完成訓練金絲猴的圖片後，按一下B鍵，未來板就會切換至下個分類。

重複以上步驟直至完成所有分類的訓練。

<figure><img src="../../.gitbook/assets/image (291).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (292).png" alt=""><figcaption></figcaption></figure>

最後按下中間的M鍵，儲存模型。

成功儲存的話KOI 2會顯示Save Successfully的字樣, 表示模型已經成功儲存。

<figure><img src="../../.gitbook/assets/image (293).png" alt=""><figcaption></figcaption></figure>

## 2. 中華瀕危物種AI鑒別器使用教學

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

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

未來板會顯示辨認到的動物名稱。

按未來板的B鍵，生成式AI就會生成一段文字介紹該動物並以粵語朗讀出來。

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

按下中間的M鍵，未來板就會顯示Listening。向未來板說出你的問題，未來板會將進行語音辨識。

<figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

生成式AI就會生成出答案並以粵語朗讀出來。

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

### 更改WiFI登入資料

如需更改WiFi的登入資料，請打開wifi.txt然後輸入新的SSID和密碼，兩者用逗號( , )分隔。

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>
