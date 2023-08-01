---
description: 溫濕度魔塊 (HKBM8012D)
---

# 溫濕度魔塊

![](https://kittenbothk.readthedocs.io/en/latest/\_images/05\_05.png)

此模塊用於探測環境的溫度和濕度。附有3pin防反插接口，可以加插雨滴或土壤魔塊。

### 詳細介紹

![](https://kittenbothk.readthedocs.io/en/latest/\_images/05\_04.png)

### 產品參數

* 支援電壓：3V-5V
* 尺寸：56mm X 24mm X 19mm
* 接口：4pin防反插接口；3PIN防反插接口。
* 溫度測量範圍：0-50°C，精準度±2°C
* 濕度測量範圍：20-90%RH，精準度±5%RH
* 模擬數值測量範圍(雨滴或土壤魔塊)：0-1023

### 使用注意事項

* 這魔塊不能放入水中，放入水中會導致短路。

### 接線方法

將溫濕度魔塊用4pin排線連接至Armourbit。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/env\_wire.png)

### MakeCode編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner13.png)

#### 加載PowerBrick插件：

#### 在擴展頁直接搜尋powerbrick (PowerBrick已經過微軟認證，可以直接搜尋)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/powerbrick\_search.png)

#### 你亦可以用插件地址搜尋

PowerBrick插件地址：https://github.com/KittenBot/pxt-powerbrick

#### [詳細方法](../../ge-bian-cheng-ping-tai-jie-shao/makecode/kittenbotandmakecode.md)

#### 溫濕度魔塊積木塊:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/environmentblocks.png)

#### 溫度測量編程

{% embed url="https://makecode.microbit.org/_7iaJkbDr3H0J" %}

[參考程式網址](https://makecode.microbit.org/\_7iaJkbDr3H0J)

#### 相對濕度測量編程

{% embed url="https://makecode.microbit.org/_iwp6isU4hLRR" %}

[參考程式網址](https://makecode.microbit.org/\_iwp6isU4hLRR)

#### Makecode教學短片

{% embed url="https://www.youtube.com/watch?v=ilXSpFd86DQ" %}

### 插件版本與更新

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../../ge-bian-cheng-ping-tai-jie-shao/makecode/makecodeextupdate.md)

### KittenBlock編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbbanner7.png)

#### 加載PowerBrick插件

在左上角小貓logo旁邊的硬件欄選擇PowerBrick，加載Microbit與Powerbrick插件。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/addextension1.png)

#### 環境積木塊

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbenvblocks.png)

#### 溫度測量編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbtemp.png)

[參考程式下載](https://bit.ly/PowerbrickM1\_01sb3)

#### 相對濕度測量編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbhumid.png)

[參考程式下載](https://bit.ly/PowerbrickM1\_02sb3)

### FAQ

1：為什麼我點擊積木塊沒有反應呢？

首先確保已經連接好Microbit，然後上載韌體再試一試。
