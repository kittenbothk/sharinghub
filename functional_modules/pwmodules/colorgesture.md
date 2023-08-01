---
description: 顏色及手勢魔塊 (HKBM8012F)
---

# 顏色及手勢魔塊

![](https://kittenbothk.readthedocs.io/en/latest/\_images/09\_06.png)

這是一塊多功能的魔塊，它的主要功能是識別顏色和識別手勢。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/IMG\_2572.GIF)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/IMG\_2573.GIF)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/IMG\_2574.GIF)

它有4種模式：

1. 在顏色辨識模式下，4顆LED會常亮，檢測顏色的色環角度。它還可以檢測環境光度。
2. 在手勢辨識模式下，手的移動方向會觸發對應方向的LED閃動。
3. 在距離檢測模式下，最遠範圍為大約3cm。距離越近，LED越亮。
4. 在LED模式下，可以控制4顆LED的亮度。

### 詳細介紹

![](https://kittenbothk.readthedocs.io/en/latest/\_images/09\_05.png)

### 產品參數

* 支援電壓：3V-5V
* 尺寸：56mm X 24mm X 16mm
* 接口：4pin防反插接口
* 顏色識別檢測返回值：0－360
* 手勢識別模式下，可識別上下左右四個方向，分別返回1、2、3、4。偵測不到手勢則返回0。
* 距離檢測模式下，最大檢測距離為3cm左右，返回值為0-255，越靠近數值越大。
* 亮度檢測返回值：0-255

### 使用注意事項

* 這魔塊只能連接到I2C接口，其他接口無效。
* 使用前要先設置模式，否則默認為距離模式。
* 手勢模式下，你可能需要熟習一下手移動的方向、距離和速度才掌握到觸發技巧。
* 顏色辨認會返回HSV角度數值，並非RGB數值。
* 顏色辨認的距離為大約1cm時的效果最為理想。
* 在LED模式之下才可以控制LED的亮度。

### 接線方法

#### Armourbit

將顏色手勢魔塊用4pin排線連接至Armourbit的I2C接口。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/color\_wire.png)

#### Robotbit

將顏色手勢魔塊連接至Robotbit的I2C接口。

```
藍色線（A）請接到SCL，綠色線（B）請接到SDA。
```

![](https://kittenbothk.readthedocs.io/en/latest/\_images/gesture\_wire1.png)

### MakeCode編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner13.png)

#### 加載PowerBrick插件：

#### 在擴展頁直接搜尋powerbrick (PowerBrick已經過微軟認證，可以直接搜尋)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/powerbrick\_search.png)

#### 你亦可以用插件地址搜尋

PowerBrick插件地址：https://github.com/KittenBot/pxt-powerbrick

#### [詳細方法](../../ge-bian-cheng-ping-tai-jie-shao/makecode/kittenbotandmakecode.md)

#### 顏色手勢魔塊積木塊:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/colorgestureblocks1.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/colorgestureblocks2.png)

#### 顏色檢測

{% embed url="https://makecode.microbit.org/_LLbfYx40CEdX" %}

[參考程式網址](https://makecode.microbit.org/\_LLbfYx40CEdX)

HSV色環可以參考下圖：

![](https://kittenbothk.readthedocs.io/en/latest/\_images/hsv.jpg)

#### 亮度檢測

{% embed url="https://makecode.microbit.org/_LTt5ugP2f00K" %}

[參考程式網址](https://makecode.microbit.org/\_LTt5ugP2f00K)

#### 距離檢測

{% embed url="https://makecode.microbit.org/_RhKfYUJwu0AK" %}

[參考程式網址](https://makecode.microbit.org/\_RhKfYUJwu0AK)

#### 手勢檢測

{% embed url="https://makecode.microbit.org/_4eiKzMXot5Vy" %}

[參考程式網址](https://makecode.microbit.org/\_4eiKzMXot5Vy)

#### LED控制

{% embed url="https://makecode.microbit.org/_c5s6sFH3mgXY" %}

[參考程式網址](https://makecode.microbit.org/\_c5s6sFH3mgXY)

#### Makecode教學短片

{% embed url="https://www.youtube.com/watch?v=7WrkDYMc2f0" %}

#### 示範短片

{% embed url="https://www.youtube.com/watch?v=jhGaRx7EGms" %}

{% embed url="https://www.youtube.com/watch?v=BWK_pLO0qpA" %}

{% embed url="https://www.youtube.com/watch?v=UTiFh02MpMc" %}

### 插件版本與更新

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../../ge-bian-cheng-ping-tai-jie-shao/makecode/makecodeextupdate.md)

### KittenBlock編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbbanner7.png)

#### 加載PowerBrick插件

在左上角小貓logo旁邊的硬件欄選擇PowerBrick，加載Microbit與Powerbrick插件。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/addextension1.png)

#### 顏色手勢魔塊積木塊

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbcolorgestureblocks.png)

#### 顏色檢測

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbcolor.png)

[參考程式下載](https://bit.ly/PowerbrickM7\_01sb3)

#### 亮度檢測

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbbrightness.png)

[參考程式下載](https://bit.ly/PowerbrickM7\_02sb3)

#### 距離檢測

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbcolordist.png)

[參考程式下載](https://bit.ly/PowerbrickM7\_03sb3)

#### 手勢檢測

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbgesture.png)

[參考程式下載](https://bit.ly/PowerbrickM7\_04sb3)

#### LED控制

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbled.png)

[參考程式下載](https://bit.ly/PowerbrickM7\_05sb3)

### FAQ

1：為什麼我點擊積木塊沒有反應呢？

首先確保已經連接好Microbit，然後上載韌體再試一試。
