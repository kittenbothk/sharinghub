---
description: x8 LED 全彩魔屏 (HKBM8012J)
---

# 8x8 LED 全彩魔屏

![](https://kittenbothk.readthedocs.io/en/latest/\_images/11\_04.png)

這是一塊8x8的全彩魔屏，可以單獨控制任意一點的顏色或者整個屏幕的顏色。支持多塊魔屏串聯，组成16x16或者8x32等魔屏，令顯示效果更加豐富。

### 詳細介紹

![](https://kittenbothk.readthedocs.io/en/latest/\_images/11\_03.png)

### 產品參數

* 支援電壓：3V-5V
* 尺寸：56mm X 24mm X 16mm
* 接口：4pin防反插接口
* 像素：8x8全彩

### 使用注意事項

* 魔屏上有兩個接口，輸入和輸出，單獨使用，請使用輸入接口與Armourbit連接。
* 魔屏進行串聯需要將第一塊魔屏的輸出與下一塊的輸入接口連接。
* 用電池盒時最多支援串聯4塊魔屏。如需接更多，需外接電源，或者降低點陣亮度，以此減少電流。
* 長時間使用彩色魔屏請注意散熱。

### 接線方法

將點陣魔塊用4pin排線連接至Armourbit。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/rgb\_wire.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/11\_25.png)

### MakeCode編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner13.png)

#### 加載PowerBrick插件：

#### 在擴展頁直接搜尋powerbrick (PowerBrick已經過微軟認證，可以直接搜尋)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/powerbrick\_search.png)

#### 你亦可以用插件地址搜尋

PowerBrick插件地址：https://github.com/KittenBot/pxt-powerbrick

#### [詳細方法](../../makecode/kittenbotandmakecode.md)

#### 點陣魔塊積木塊

![](https://kittenbothk.readthedocs.io/en/latest/\_images/rgbblocks1.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/rgbblocks2.png)

#### 單色點亮

{% embed url="https://makecode.microbit.org/_dgdfa73fb6jr" %}

[參考程式網址](https://makecode.microbit.org/\_dgdfa73fb6jr)

#### 彩虹色點亮

{% embed url="https://makecode.microbit.org/_VDtaD6AVjfdd" %}

[參考程式網址](https://makecode.microbit.org/\_VDtaD6AVjfdd)

#### 單顆燈點亮

{% embed url="https://makecode.microbit.org/_iv6MHWEkDMjr" %}

[參考程式網址](https://makecode.microbit.org/\_iv6MHWEkDMjr)

#### 圖案點亮示範

{% embed url="https://makecode.microbit.org/_2cF73496m8p1" %}

[參考程式網址](https://makecode.microbit.org/\_2cF73496m8p1)

#### Makecode教學短片

{% embed url="https://www.youtube.com/watch?v=Pmg6Gvg29jo" %}

### 插件版本與更新

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../../makecode/makecodeextupdate.md)

### KittenBlock編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbbanner7.png)

#### 加載PowerBrick插件

在左上角小貓logo旁邊的硬件欄選擇PowerBrick，加載Microbit與Powerbrick插件。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/addextension1.png)

#### 點陣魔塊積木塊

![](https://kittenbothk.readthedocs.io/en/latest/\_images/rgbblocks.png)

#### 逐顆點亮

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbrgb.png)

[參考程式下載](https://bit.ly/PowerbrickM9\_01sb3)

由於顯示色彩只支援RGB，假如你有一組HSV顏色，你必需要將其轉換至RGB格式。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/HSVTORGB.png)

### FAQ

1：為什麼我點擊積木塊沒有反應呢？

首先確保已經連接好Microbit，然後上載韌體再試一試。
