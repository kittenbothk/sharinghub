---
description: T/T減速直流電機(HKBD8004B)
---

# T/T減速直流電機

![](https://kittenbothk.readthedocs.io/en/latest/\_images/TT.png)

這是一款減速直流電機，特點在於扭力高噪音低。

相較市面的TT馬達質量更有保證，相同轉速下電流更小，轉動方向和速度可調控：接線處包上橡膠，避免接線因拉扯而脫落，保護性更佳。

### 產品參數

* 工作電壓：3.3V\~6V
* 額定電壓：4.8V
* 額定電流：200mA
* 堵轉電流：1800mA
* 最高轉速：200rpm
* 停止扭力：1000g
* 齒輪比： 1:48
* 接口：紅黑線，防反插接口

### 接線方法

#### ArmourBit

將電機的紅黑線連接至Armourbit底部的電機接口。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/tt\_wire2.png)

```
沒有嚴格正負極之分，插的方向只會影響電機轉動方向。
```

#### RobotBit

將電機的紅黑線連接至RobotBit的電機接口。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/tt\_wire1.png)

![.](https://kittenbothk.readthedocs.io/en/latest/\_images/2kmotorConRB11.jpg)

```
沒有嚴格正負極之分，插的方向只會影響電機轉動方向。
```

### MakeCode編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner17.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/acbanner3.png)

#### 此模組可供Microbit和Meowbit使用。

#### ArmourBit

#### 加載Powerbrick插件：

#### 在擴展頁直接搜尋Powerbrick (powerbrick已經過微軟認證，可以直接搜尋)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/powerbrick\_search2.png)

#### [詳細方法](../ge-bian-cheng-ping-tai-jie-shao/makecode/kittenbotandmakecode.md)

#### 電機積木塊:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/motorblocks1.png)

### 電機編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/motor1.png)

[參考程式下載](https://bit.ly/PowerbrickM11\_01Hex)

[參考程式網址](https://makecode.microbit.org/\_RYHivyayYL4q)

#### Makecode教學短片

{% embed url="https://www.youtube.com/watch?v=gUR2DbgVTCQ" %}

#### RobotBit

#### 加載RobotBit插件：

![](https://kittenbothk.readthedocs.io/en/latest/\_images/robotbitExtension.png)

#### [詳細方法](../ge-bian-cheng-ping-tai-jie-shao/makecode/kittenbotandmakecode.md)

#### 電機積木塊:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/2kmotorblocks\_rb1.png)

#### 電機編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/2kmotorcode\_rb1.png)

[參考程式網址](https://makecode.microbit.org/\_33HMywgx9H97q)

#### Meowbit:

#### 加載robotbit插件：https://github.com/KittenBot/meow-robotbit

#### [詳細方法](../ge-bian-cheng-ping-tai-jie-shao/makecode/kittenbotandmakecode.md)

#### 電機積木塊:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/motorblocks2.png)

### 電機編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/2kmotorcode\_meow1.png)

[參考程式網址](https://makecode.com/\_2z0C8v6XAC5y)

### 插件版本與更新

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../ge-bian-cheng-ping-tai-jie-shao/makecode/makecodeextupdate.md)

### KittenBlock編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbbanner12.png)

#### 這教學使用Microbit作例子，每款擴展板/主控板的使用教學請參考相應頁面。

#### Armourbit

#### 加載PowerBrick插件

在左上角小貓logo旁邊的硬件欄選擇PowerBrick，加載Microbit與Powerbrick插件。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/addextension3.png)

#### 電機積木塊

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbmotorblocks\_armourbit1.png)

#### 電機編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/9gmotor\_armourbit\_kb\_code1.png)

[參考程式下載](https://bit.ly/PowerbrickM11\_01sb3)

#### Robotbit

#### 加載Robotbit插件

在左上角小貓logo旁邊的硬件欄選擇Microbit，加載Microbit與Robotbit插件。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/addRB3.png)

#### 電機積木塊

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbmotorblocks1.png)

#### 電機編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/9gmotor\_robotbit\_kb\_code1.png)

### FAQ

1：為什麼我點擊積木塊沒有反應呢？

首先確保已經連接好Microbit，然後上載韌體再試一試。
