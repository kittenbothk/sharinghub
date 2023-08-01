# 人臉檢測追蹤

人臉檢測追蹤的應用廣範，本節教程教大家如何將人臉位置反映在Microbit的點陣上

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/08.png" alt=""><figcaption></figcaption></figure>

### 編寫人臉檢測追蹤程式[¶](broken-reference)

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/mcbanner.png" alt=""><figcaption></figcaption></figure>

#### 加載KOI插件：[¶](broken-reference)

#### 在擴展頁直接搜尋KOI (KOI已經過微軟認證，可以直接搜尋)[¶](broken-reference)

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/koi_search.png" alt=""><figcaption></figcaption></figure>

#### 你亦可以用插件地址搜尋[¶](broken-reference)

KOI插件：https://github.com/KittenBot/pxt-KOI

人臉檢測積木塊：

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/09.png" alt=""><figcaption></figcaption></figure>

编寫參考程式：

{% embed url="https://makecode.microbit.org/_8A3FkRX83gfo" %}

### 程式流程[¶](broken-reference)

把程式下載到Microbit上，可以看到Microbit的點陣隨著人臉的移動而移動。

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/04-13.png" alt=""><figcaption></figcaption></figure>

### 改變點陣的映射方向[¶](broken-reference)

在某些情況下，如果你想改變的LED移動方向，將“低至4至高0”更改為“低至0至高4”

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/023.png" alt=""><figcaption></figcaption></figure>

### 插件版本與更新[¶](broken-reference)

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../../../makecode/makecodeextupdate.md)

### FAQ[¶](broken-reference)

#### 1: 為什麼我重新打開電源，模組螢幕顯示“Yolo not loaded”，貌似hang機狀態, 並且每次如是?[¶](broken-reference)

· 答：打開電源後, KOI 及microbit 同時起動; 相對上, Microbit 所需的起動時間比KOI魔塊短, 引致 Microbit的初始化程式（串口指令中, 控制載入Yolo模型）已經跑完了，KOI還沒完全起動, 最後會在螢幕中呈現報錯資訊。

· 解決辦法：打開電源後，重新按下Microbit背後的Reset按鍵，讓Microbit重新開始運行（秘訣就是讓KOI魔塊先完全運行起來，再讓Microbit 跑初始化程式）

#### 2: KOI鯉魚魔塊我直接3V電源可以嗎？[¶](broken-reference)

· 答：不行，必須要接5V！
