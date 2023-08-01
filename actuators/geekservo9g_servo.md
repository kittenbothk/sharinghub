---
description: Geekservo舵機 (HKBD8005A)
---

# Geekservo 9g舵機

![](https://kittenbothk.readthedocs.io/en/latest/\_images/13\_04.png)

這是一款兼容樂高件的舵機。輸出軸為樂高十字軸。主要用在需求精細控制的結構上，例如關節，機械臂。

### 產品參數

* 工作電壓：3.3V\~6V
* 額定電壓：4.8V
* 額定電流：200ma
* 堵轉電流：700ma
* 打滑電流：450ma
* 最大扭力：500g/cm(4.8V)
* 角度轉速：60°/0.12s
* 角度範圍：-45°\~225°
* 重量：12.4g
* 接口：橙紅啡線

### 使用注意事項

* 這只是一種小型電機，使用情境的扭力和電壓需求請不要過大。
* Geekservo舵機有嚴格的線序要求，請根據線序連接。
* 禁止長時間超出堵轉電流，否則會燒壞電機。

### 規格尺寸

#### 樂高孔單位:

* 長度：5孔
* 闊度：2孔
* 高度：3孔
* 輸出軸：樂高十字軸

#### mm單位:

* 長度：40mm
* 闊度：16mm
* 高度：34.4mm
* 輸出軸：樂高十字軸

![](https://kittenbothk.readthedocs.io/en/latest/\_images/13\_03.png)

### Geekservo特色

* 極力子過載保護:
  * 遇到輸出軸被暴力扭擰會啟動極力子進行跳齒保護，發出「噠噠噠」的聲音。不會損毀齒輪。
* 安裝方式靈活:
  * 支援樂高標準磚和Technic插孔，輸出軸亦是樂高標準十字軸。
* 輕盈小巧:
  * 方便製作各種小型機械。

### 接線方法

#### ArmourBit

將舵機的橙紅啡線連接至Armourbit背部的舵機接口。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/servo\_wire3.png)

```
啡色接負極，紅色接正極，橙色接數據。
```

#### RobotBit

將舵機的橙紅啡線連接至RobotBit的舵機接口。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/servoConRB.jpg)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/2kservoConRB1.jpg)

```
啡色接負極，紅色接正極，橙色接數據
```

### MakeCode編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner17.png)

#### 此模組可供Microbit和Meowbit使用。

### ArmourBit

#### 加載Powerbrick插件：

#### 在擴展頁直接搜尋Powerbrick (powerbrick已經過微軟認證，可以直接搜尋)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/powerbrick\_search2.png)

#### [詳細方法](../ge-bian-cheng-ping-tai-jie-shao/makecode/kittenbotandmakecode.md)

#### 舵機編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/9gservo\_code.png)

[參考程式網址](https://makecode.microbit.org/\_DzFfzKPmuM4s)

### RobotBit

#### 加載RobotBit插件：

![](https://kittenbothk.readthedocs.io/en/latest/\_images/robotbitExtension.png)

#### [詳細方法](../ge-bian-cheng-ping-tai-jie-shao/makecode/kittenbotandmakecode.md)

#### 舵機積木塊:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/servoblocks.png)

#### 舵機編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/9gservo\_code.png)

[參考程式網址](https://makecode.microbit.org/\_YfJdx4FRx2eP)

#### Makecode教學短片

{% embed url="https://www.youtube.com/watch?v=gUR2DbgVTCQ" %}

#### Meowbit:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/acbanner3.png)

#### 加載robotbit插件：https://github.com/KittenBot/meow-robotbit

#### [詳細方法](../ge-bian-cheng-ping-tai-jie-shao/makecode/kittenbotandmakecode.md)

#### 電機積木塊:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/motorblocks2.png)

### 電機編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/9gservo\_code\_meow.png)

[參考程式網址](https://makecode.com/\_WrrEcRhMm0o4)

### 插件版本與更新

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../ge-bian-cheng-ping-tai-jie-shao/makecode/makecodeextupdate.md)

### KittenBlock編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbbanner12.png)

#### 這教學使用Microbit作例子，每款擴展板/主控板的使用教學請參考相應頁面。

#### Armourbit，Robotbit與Meowbit編程方法一樣，請加載相應插件

#### Armourbit

#### 加載PowerBrick插件

在左上角小貓logo旁邊的硬件欄選擇PowerBrick，加載Microbit與Powerbrick插件。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/addextension3.png)

#### 舵機積木塊

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbservoblocks\_armourbit.png)

#### 舵機編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/9gservo\_armourbit\_kb\_code.png)

[參考程式下載](https://bit.ly/PowerbrickM12\_01sb3)

#### Robotbit

#### 加載Robotbit插件

在左上角小貓logo旁邊的硬件欄選擇Microbit，加載Microbit與Robotbit插件。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/addRB3.png)

#### 舵機積木塊

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbservoblocks.png)

#### 舵機編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/9gservo\_robotbit\_kb\_code.png)

### FAQ

1：為什麼我點擊積木塊沒有反應呢？

首先確保已經連接好Microbit，然後上載韌體再試一試。
