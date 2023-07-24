# 方形追踪

### 編寫方形追踪程式[¶](broken-reference)

#### 加載KOI插件：[¶](broken-reference)

#### 在擴展頁直接搜尋KOI (KOI已經過微軟認證，可以直接搜尋)[¶](broken-reference)

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/koi_search.png" alt=""><figcaption></figcaption></figure>

#### 你亦可以用插件地址搜尋[¶](broken-reference)

KOI插件：https://github.com/KittenBot/pxt-KOI

方形追踪積木塊：

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/01-12.png" alt=""><figcaption></figcaption></figure>

完整參考程式：

{% embed url="https://makecode.microbit.org/_HaYX6MH8VAD5" %}

#### 臨界值[¶](broken-reference)

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/04-12.png" alt=""><figcaption></figcaption></figure>

臨界值是影響識別率的一個參數, 需要自主嘗試並調整臨界值。

臨界值越大，干擾越少，但識別難度也會提高。因此需要自己根據場景多做測試。

### 程式運行流程[¶](broken-reference)

程式下載到Microbit 上, 按下Microbit 上的A鍵. KOI 的螢幕上顯示出左下角的x, y 位置值, 還有當時測得的長度與寬度 (KOI 螢幕單位佔比計算)

### 進階程式[¶](broken-reference)

為方便讀取方形資訊, 我們便可考慮多加一塊OLED顯示屏, 以提高資訊的可讀性。

#### OLED接線[¶](broken-reference)

本例子以Robotbit 示範, 把OLED 屏接到I2C 接口上

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/03-1.png" alt=""><figcaption></figcaption></figure>

#### 編寫程式[¶](broken-reference)

{% embed url="https://makecode.microbit.org/_LmE8H5efoffA" %}

### 插件版本與更新[¶](broken-reference)

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考:[ Makecode插件版本更換](../../makecode/makecodeextupdate.md)

### FAQ[¶](broken-reference)

#### 1: 為什麼我打開電源，按Microbit的A按鍵，怎麼沒反應？[¶](broken-reference)

​ · 答：打開電源後, KOI 及microbit 同時起動; 相對上, Microbit 所需的起動時間比KOI魔塊短, 引致 Microbit 的初始化程式已經跑完了，KOI還沒完全起動。

​ · 解決辦法：打開電源後，重新按下Microbit背後的Reset按鍵，讓Microbit重新開始運行（秘訣就是讓KOI魔塊先完全運行起來，再讓Microbit 跑初始化程式）

#### 2: 如何提高識別率[¶](broken-reference)

· 調整識別閾值，調整識別環境與調整識別物體;

· 識別背景盡量單調，不能太雜亂;

· 方形有銳利的輪廓。
