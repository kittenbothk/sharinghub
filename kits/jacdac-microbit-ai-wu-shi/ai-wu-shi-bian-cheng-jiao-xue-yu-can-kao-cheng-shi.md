# AI巫師 編程教學與參考程式

## 編程教學

### CreateAI手勢機器學習

CreateAI是專為Micro:bit而設計的機器學習平台，學生可以訓練Micro:bit使用陀螺儀加速器的數據辨認不同動作。

<figure><img src="../../.gitbook/assets/Screenshot 2025-10-14 162013.png" alt=""><figcaption></figcaption></figure>

打開CreateAI的頁面。

{% embed url="https://createai.microbit.org/" %}

按Get Started，按New Session。

<figure><img src="../../.gitbook/assets/Screenshot 2025-10-14 162926.png" alt=""><figcaption></figcaption></figure>

使用USB線連接Micro:bit到電腦。

點擊Connect。

<figure><img src="../../.gitbook/assets/Screenshot 2025-10-14 163210.png" alt=""><figcaption></figcaption></figure>

按照指示，將hex檔下載到Microbit

<div><figure><img src="../../.gitbook/assets/Screenshot 2025-10-14 163305.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Screenshot 2025-10-14 163405.png" alt=""><figcaption></figcaption></figure></div>

拔除USB線並打開電池盒開關。Micro:bit會顯示1組圖案。選擇Microbit顯示的圖案然後按Next。

<div><figure><img src="../../.gitbook/assets/Screenshot 2025-10-14 163447.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Screenshot 2025-10-14 163718.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Screenshot 2025-10-14 163700.png" alt=""><figcaption></figcaption></figure></div>

成功連接後，可以在頁面看到Micro:bit實時的陀螺儀數值。

<figure><img src="../../.gitbook/assets/Screenshot 2025-10-14 163752.png" alt=""><figcaption></figcaption></figure>

輸入第一個動作的名稱，然後就可以開始訓練。

<figure><img src="../../.gitbook/assets/Screenshot 2025-10-14 164044.png" alt=""><figcaption></figcaption></figure>

按B鍵，頁面會開始倒數3 2 1 Go，當頁面顯示Recording的時候就可以做出動作。頁面會記錄這個動作的陀螺儀數值，重複訓練直至分類有至少3個訓練數據。

<div><figure><img src="../../.gitbook/assets/Screenshot 2025-10-14 164424.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Screenshot 2025-10-14 164437.png" alt=""><figcaption></figcaption></figure></div>

可以以圖表的方式看到Microbit記錄的數據，請確保每個數據的圖表形狀都類似，如有不同形狀的數據，請按交叉刪除並重新訓練。

<figure><img src="../../.gitbook/assets/Screenshot 2025-10-14 170901.png" alt=""><figcaption></figcaption></figure>

按Add Action就可以添加動作分類，重複訓練步驟，記錄所有動作的數據。

<div><figure><img src="../../.gitbook/assets/image (187).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (189).png" alt=""><figcaption></figcaption></figure></div>

完成所有數據紀錄之後就可以按Train Model訓練模型。

<div><figure><img src="../../.gitbook/assets/image (188).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (190).png" alt=""><figcaption></figcaption></figure></div>

訓練完成後可以在線測試模型，假如模型結果理想就可以按Edit In MakeCode開始編程。

<figure><img src="../../.gitbook/assets/image (191).png" alt=""><figcaption></figcaption></figure>

在MakeCode裏會新增一個Machine Learning的分類，當Microbit偵測到特定動作後就會觸發相應指令。

<figure><img src="../../.gitbook/assets/image (192).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (198).png" alt=""><figcaption></figcaption></figure>

完成編程後就可以將程式下載到Micro:bit。下載時頁面會彈出提示，由於程式下載會覆蓋Microbit原有的程式，所以如果你把程式下載到訓練所用的Microbit後，你想再次記錄動作數據的話就需要重複一次連接Microbit的步驟。

<figure><img src="../../.gitbook/assets/image (193).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (194).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;">我們建議你儲存這次CreateAI的專案，方便你日後使用/修改。</mark>

您可以將專案Download as File，專案就會以hex檔的形式儲存下來。然後在CreateAI的頁面中可以按Continue載入hex檔，所有的訓練數據和編程積木都會加載得到。

<figure><img src="../../.gitbook/assets/image (195).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../../.gitbook/assets/image (196).png" alt=""><figcaption></figcaption></figure>

下載下來的hex檔亦可以在Makecode平台打開，訓練好的模型和編程積木都不會損失。不過在Makecode平台上就不能進行任何模型訓練或數據的紀錄。

<figure><img src="../../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>

### Jacdac模組控制

## 參考程式

### 魔法棒

{% hint style="info" %}
此參考程式已包括已訓練好的機器學習模型，假如需要自行訓練，請參考編程教學篇章。
{% endhint %}

{% embed url="https://makecode.microbit.org/_aoj8YKRE8Pwc" %}

[參考程式](https://makecode.microbit.org/_aoj8YKRE8Pwc)

### 展示板

{% embed url="https://makecode.microbit.org/_8Heb086EmVEt" %}

[參考程式](https://makecode.microbit.org/_8Heb086EmVEt)
