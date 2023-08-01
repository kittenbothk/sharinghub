# 人面辨識 (固件版本: v1.9.5或之後)

人面檢測和人面辨識在於前者只是探測畫面是否有人面，而後者可以將人面記下來並可以辨認該人面。在KOI也可以做到人面辨識的功能。

### 編寫人面辨識程式[¶](broken-reference)

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/mcbanner.png" alt=""><figcaption></figcaption></figure>

#### 加載KOI插件：[¶](broken-reference)

#### 在擴展頁直接搜尋KOI (KOI已經過微軟認證，可以直接搜尋)[¶](broken-reference)

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/koi_search.png" alt=""><figcaption></figcaption></figure>

#### 你亦可以用插件地址搜尋[¶](broken-reference)

KOI插件：https://github.com/KittenBot/pxt-KOI

人面辨識積木塊：

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/12.png" alt=""><figcaption></figcaption></figure>

編寫程式：

{% embed url="https://makecode.microbit.org/_8TWcRzY2j1ui" %}

```
人臉辨識需要連接WIFI。假如你已經入網，之後不需要每次都運行入網的積木。

由於這個功能是免費的，你使用的人臉組名稱可能有人已用過，所以請選擇一個比較獨特的名稱。
例如Test123這種就可能有人已經用過了。
另外，在人臉組裏面最多可以儲存20張人臉照片。
```

### 程式流程[¶](broken-reference)

1: 首先將程式下載到Microbit上。

2: 將人面對準鏡頭然後按下A按鍵錄入人面。

3: KOI需要一段短時間分析畫面，成功分析之後畫面會顯示人臉的年齡和性別。

4: 按下A和B按鍵，錄入下一張人臉。

5: 重複2-4。

6: 錄完之後可以按下B按鍵開始辨識人臉。

7: 辨識到之後畫面就會列出人臉的名稱和準繩度。假如遇到未被錄入的人臉，KOI就會顯示Stranger字句。

```
準繩度由0-100，越高越準確。
```

### 插件版本與更新[¶](broken-reference)

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../../../ge-bian-cheng-ping-tai-jie-shao/makecode/makecodeextupdate.md)

### FAQ[¶](broken-reference)

#### 1： 為什麼我重新開機，按下按鍵A，但按鍵沒有反應？[¶](broken-reference)

· 答：打開電源後, KOI 及microbit 同時起動; 相對上, Microbit 所需的起動時間比KOI魔塊短, 引致 Microbit的初始化程式已經跑完了，KOI還沒完全起動, 因此按下A鍵沒有反應。

· 解決辦法：打開電源後，重新按下Microbit背後的Reset按鍵，讓Microbit重新開始運行（秘訣就是讓KOI魔塊先完全運行起來，再讓Microbit 跑初始化程式）

#### 2： KOI鯉魚魔塊我直接3V電源可以嗎？[¶](broken-reference)

· 答：不行，必須要接5V！

#### 3: 拍照之後KOI出現紅字，顯示 “Pic not has face” ，是我做錯了嗎？[¶](broken-reference)

· 答：是正常的，這只是因為拍照的時候可能對焦未清楚或者有震動所以模糊了，只要再拍一次就可以了。

#### 3: 拍照之後KOI出現紅字，顯示 “Get Timeout” ，是我做錯了嗎？[¶](broken-reference)

· 答：有時候網絡不穩定、網絡擠塞或者伺服器忙碌的時候就會顯示Get Timeout，請再拍一次。
