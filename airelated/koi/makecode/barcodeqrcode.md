# 讀取條碼Bar Code 及 二維碼QR Code

· 條碼 (Bar Code) 廣泛用於我們生活中，例如產品的識別標籤。

· 二維碼(QR Code)用於支付場景或者社交場景。

### 編寫Bar Code及QR Code讀取程式[¶](broken-reference)

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/mcbanner.png" alt=""><figcaption></figcaption></figure>

#### 加載KOI插件：[¶](broken-reference)

#### 在擴展頁直接搜尋KOI (KOI已經過微軟認證，可以直接搜尋)[¶](broken-reference)

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/koi_search.png" alt=""><figcaption></figcaption></figure>

#### 你亦可以用插件地址搜尋[¶](broken-reference)

KOI插件：https://github.com/KittenBot/pxt-KOIa

讀取標籤積木塊：

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/014.png" alt=""><figcaption></figcaption></figure>

完整參考程式：

{% embed url="https://makecode.microbit.org/_gckdFPXUEgto" %}

### 程式運行流程[¶](broken-reference)

把程式下載到Microbit 上,

1. 把Bar Code 放到KOI 鏡頭前, 按下Microbit的按鍵A，進行識別; Bar Code 數字便會顯示在KOI 的螢幕上。
2. 把QR Code 放到KOI 鏡頭前, 按下Microbit的按鍵B，進行識別; QR Code 所含的資訊便會顯示在KOI 的螢幕上。

### 進階程式[¶](broken-reference)

讀取Bar Code 及 QR Code 後可能出現大量資訊, 在KOI 的螢幕上未必有足夠時間閱讀; 此時我們便可考慮多加一塊OLED顯示屏, 以提高資訊的可讀性。

#### OLED接線[¶](broken-reference)

本例子以Robotbit 示範, 把OLED 屏接到I2C 接口上

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/03-1.png" alt=""><figcaption></figcaption></figure>

#### 編寫程式[¶](broken-reference)

{% embed url="https://makecode.microbit.org/_bXFegEPx6Vv7" %}

### 插件版本與更新[¶](broken-reference)

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../../../ge-bian-cheng-ping-tai-jie-shao/makecode/makecodeextupdate.md)

### FAQ[¶](broken-reference)

#### 1: 為什麼我打開電源，按Microbit的A按鍵，怎麼沒反應？[¶](broken-reference)

​ · 答：打開電源後, KOI 及microbit 同時起動; 相對上, Microbit 所需的起動時間比KOI魔塊短, 引致 Microbit 的初始化程式已經跑完了，KOI還沒完全起動。

​ · 解決辦法：打開電源後，重新按下Microbit背後的Reset按鍵，讓Microbit重新開始運行（秘訣就是讓KOI魔塊先完全運行起來，再讓Microbit 跑初始化程式）

#### 2: 為什麼不能成功讀取Bar Code 或QR Code？[¶](broken-reference)

· 答：條碼及二維碼的寬度要求不小於3.5cm; 若條碼太小，會因解析度太小的原因無法識別。另掃描時保證完全條碼或二維碼入鏡且清晰。
