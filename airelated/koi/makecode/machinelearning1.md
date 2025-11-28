# 機器學習–自定義物件識別（模型訓練）

機器學習（Machine Learning）聽起來好像一個很遙遠，高攀不起的課題。其實AI鏡頭已經搭載機器學習的功能，能夠分析物件特徵，容許自定義物件辨識。

在本節教程，大家將會學到如何使用內建的機器學習功能，輕鬆簡易地為機器學習模型進行訓練。

### 插入MicroSD卡[¶](/broken/pages/GFLf2KWt7KbsQo3kYvgs)

機器學習過程中訓練的圖像會暫存在SD卡，而且我們需要將訓練的模型儲存下來，所以使用機器學習時請確保SD卡已經插在卡槽。

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/022.png" alt=""><figcaption></figcaption></figure>

### 編寫模型訓練程式[¶](/broken/pages/GFLf2KWt7KbsQo3kYvgs)

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/mcbanner.png" alt=""><figcaption></figcaption></figure>

#### 加載KOI插件：[¶](/broken/pages/GFLf2KWt7KbsQo3kYvgs)

#### 在擴展頁直接搜尋KOI (KOI已經過微軟認證，可以直接搜尋)[¶](/broken/pages/GFLf2KWt7KbsQo3kYvgs)

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/koi_search.png" alt=""><figcaption></figcaption></figure>

#### 你亦可以用插件地址搜尋[¶](/broken/pages/GFLf2KWt7KbsQo3kYvgs)

KOI插件：https://github.com/KittenBot/pxt-KOI

#### 詳細方法[¶](/broken/pages/GFLf2KWt7KbsQo3kYvgs)

機器學習積木塊：

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/8.png" alt=""><figcaption></figcaption></figure>

參考程式：

{% embed url="https://makecode.microbit.org/_7wiA511Kk32h" %}

```
模型儲存的格式可以為.bin或者.json
例:aaa.json或aaa.bin
```

### 程式流程[¶](/broken/pages/GFLf2KWt7KbsQo3kYvgs)

1：將程式下載到Microbit上。

2：將第一件要辨識的物件放到鏡頭前，按下按鍵B為物件拍照，然後更換角度再按下按鍵B，直至拍下大約3張照片為止。

3：按下按鍵A開始訓練下一件物件。

4：重複步驟 2、3，直至完成所有物件的訓練。

```
參考程式設置變數flag為4，代表可以辨識4件物件，變數可以隨情況更改。

AI鏡頭支援最多40張圖片和40種物件。所以要辨識10件物件的話，每件物件最多可以拍照4張。
```

5：同時按下A和B按鍵，將模型儲存到MicroSD卡上。

```
本教程將模型命名為aaa.bin，名稱可以隨喜好更改，只要名稱以.bin或.json結尾即可。
```

### 參考短片[¶](/broken/pages/GFLf2KWt7KbsQo3kYvgs)

{% embed url="https://www.youtube.com/watch?feature=youtu.b&v=UsjingLwnHc" %}

### 插件版本與更新[¶](/broken/pages/GFLf2KWt7KbsQo3kYvgs)

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考:[ Makecode插件版本更換](../../../programmingplatforms/makecode/makecodeextupdate.md)

### FAQ[¶](/broken/pages/GFLf2KWt7KbsQo3kYvgs)

#### 1： 為什麼我重新開機，按下按鍵A，但按下A鍵沒有反應？[¶](/broken/pages/GFLf2KWt7KbsQo3kYvgs)

· 答：打開電源後, KOI 及microbit 同時起動; 相對上, Microbit 所需的起動時間比KOI魔塊短, 引致 Microbit的初始化程式已經跑完了，KOI還沒完全起動, 因此按下A鍵沒有反應。

· 解決辦法：打開電源後，重新按下Microbit背後的Reset按鍵，讓Microbit重新開始運行（秘訣就是讓KOI魔塊先完全運行起來，再讓Microbit 跑初始化程式）

#### 2： KOI鯉魚魔塊我直接3V電源可以嗎？[¶](/broken/pages/GFLf2KWt7KbsQo3kYvgs)

· 答：不行，必須要接5V！

#### 3: 為什麼我在KOI固件版本v1.8.2上嘗試訓練分類器時，螢幕出現紅字警告，不能成功訓練分類器？[¶](/broken/pages/GFLf2KWt7KbsQo3kYvgs)

· 答：KOI還未重設分類器。

· 解決辦法：使用「重置分類器」這積木手動叫KOI重置分類器。（在參考程式中，編寫了按下KOI的A按鍵手動重置分類器的功能
