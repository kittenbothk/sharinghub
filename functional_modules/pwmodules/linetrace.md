# 雙路巡線魔塊

雙路巡線魔塊 (HKBM8012B)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/07\_03.png)

這是一個紅外線巡線魔塊，它有組兩路尋線感應器，偵察到黑線後魔塊背面的LED會熄滅，觸發尋線事件。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/IMG\_2570.GIF)

### 詳細介紹

![](https://kittenbothk.readthedocs.io/en/latest/\_images/07\_01.png)

### 產品參數

* 支援電壓：3V-5V
* 尺寸：56mm X 24mm X 25mm
* 接口：4pin防反插接口

### 注意事項

* 巡線魔塊需要盡量貼近地面。
* 枱面或地板必須為不反光的表面。

### 接線方法

將巡線魔塊用4pin排線連接至Armourbit。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/linefollow\_wire.png)

### MakeCode編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner13.png)

#### 加載PowerBrick插件：

#### 在擴展頁直接搜尋powerbrick (PowerBrick已經過微軟認證，可以直接搜尋)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/powerbrick\_search.png)

#### 你亦可以用插件地址搜尋

PowerBrick插件地址：https://github.com/KittenBot/pxt-powerbrick

#### [詳細方法](../../makecode/kittenbotandmakecode.md)

#### 巡線魔塊積木塊:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/linefollowblocks.png)

#### 黑線檢測

我們在枱面貼上黑色膠紙，用巡線魔塊檢測，當感應器A或B檢測到膠紙的時候就會分別顯示笑臉或哭臉，假如沒有偵測到線條就會顯示心形。

{% embed url="https://makecode.microbit.org/_3tj8kdf8jhft" %}

[參考程式網址](https://makecode.microbit.org/\_3tj8kdf8jhft)

#### Makecode教學短片

{% embed url="https://www.youtube.com/watch?v=BT1TUlmbMm8" %}

#### 示範短片

{% embed url="https://www.youtube.com/watch?v=epcs80fGryM" %}

### 插件版本與更新

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../../makecode/makecodeextupdate.md)

### KittenBlock編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbbanner7.png)

#### 加載PowerBrick插件

在左上角小貓logo旁邊的硬件欄選擇PowerBrick，加載Microbit與Powerbrick插件。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/addextension1.png)

#### 巡線積木塊

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kblinetraceblocks.png)

#### 黑線檢測

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kblinetrace.png)

[參考程式下載](https://bit.ly/PowberbrickM5\_01sb3)

### FAQ

1：為什麼我點擊積木塊沒有反應呢？

首先確保已經連接好Microbit，然後上載韌體再試一試。
