# LCD 方向設定

KOI有個優勢，可以旋轉攝像頭，旋轉範圍0\~180°。但螢幕是不會檢測到鏡頭現在是處於前置或者後置模式，因此我們需要用程式中的積木塊進行設置。

### 编寫方向設定程式[¶](/broken/pages/2JMT8UY1hislN9Ym6JVM)

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/mcbanner.png" alt=""><figcaption></figcaption></figure>

#### 加載KOI插件：[¶](/broken/pages/2JMT8UY1hislN9Ym6JVM)

#### 在擴展頁直接搜尋KOI (KOI已經過微軟認證，可以直接搜尋)[¶](/broken/pages/2JMT8UY1hislN9Ym6JVM)

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/koi_search.png" alt=""><figcaption></figcaption></figure>

#### 你亦可以用插件地址搜尋[¶](/broken/pages/2JMT8UY1hislN9Ym6JVM)

KOI插件：https://github.com/KittenBot/pxt-KOI

方向設定積木塊：

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/011.png" alt=""><figcaption></figcaption></figure>

下拉式功能表有三個選項，分別是前置，後置，還有橫屏。

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/021.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/04.png" alt=""><figcaption></figcaption></figure>

完整參考程式：

{% embed url="https://makecode.microbit.org/_fp73TjXML9MR" %}

### 程式運行流程[¶](/broken/pages/2JMT8UY1hislN9Ym6JVM)

把程式下載到Microbit上

1: 當按下Microbit的按鍵A，Microbit點陣顯示”F“，當鏡頭與螢幕同一朝向時，圖像顯示為正。

2: 當按下Microbit的按鍵B，Microbit點陣顯”B“，當鏡頭與螢幕相反朝向時，圖像顯示為反。

### 插件版本與更新[¶](/broken/pages/2JMT8UY1hislN9Ym6JVM)

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../../../programmingplatforms/makecode/makecodeextupdate.md)

### FAQ[¶](/broken/pages/2JMT8UY1hislN9Ym6JVM)

#### 1: 為什麼我打開電源，按Microbit的AB按鍵，怎麼沒反應？[¶](/broken/pages/2JMT8UY1hislN9Ym6JVM)

· 答：打開電源後, KOI 及microbit 同時起動; 相對上, Microbit 所需的起動時間比KOI魔塊短, 引致 Microbit的初始化程式（串口指令中, 控制載入Yolo模型）已經跑完了，KOI還沒完全起動, 最後會在螢幕中呈現報錯資訊。

· 解決辦法：打開電源後，重新按下Microbit背後的Reset按鍵，讓Microbit重新開始運行（秘訣就是讓KOI魔塊先完全運行起來，再讓Microbit 跑初始化程式）

#### 2: KOI鯉魚魔塊我直接3V電源可以嗎？[¶](/broken/pages/2JMT8UY1hislN9Ym6JVM)

· 答：不行，必須要接5V！
