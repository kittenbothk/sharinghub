# OCR停車場

![](https://kittenbothk.readthedocs.io/en/latest/_images/gate1.png)

透過OCR(光學文字辨識)辨識車牌卡牌，模擬停車場自動計費系統。

### 組裝說明書下載

[組裝說明書下載](https://drive.google.com/drive/folders/1wg_edUZFrqyUONA0FJ6vFBkGArRsfnf4?usp=sharing)

![](https://kittenbothk.readthedocs.io/en/latest/_images/gate_wire1.png)

### 參考程式

{% file src="../../../.gitbook/assets/OCR停車場1.sb3" %}

<figure><img src="../../../.gitbook/assets/OCR停車場.png" alt=""><figcaption></figcaption></figure>

### 應用玩法

{% hint style="info" %}
這應用需要使用Token。
{% endhint %}

1. 連接好Micro:bit和打開Robotbit電源
2. 點擊綠色旗啟動程式
3. 將車牌卡放在鏡頭面前
4. 當超聲波感應器感應到5cm距離內有物件，程式就會進行車牌辨識
5. 程式就會記下辨識到的車牌然後打開閘門
6. 當同一個車牌再次被辨識到的時候，代表車子離開停車場，程式就會計算應付停車費



