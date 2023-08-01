---
description: Geekservo電機 (HKBD8006A)
---

# Geekservo 9g電機

![](https://kittenbothk.readthedocs.io/en/latest/\_images/13\_05.png)

這是一款兼容樂高件的減速直流電機，輸出軸為樂高十字軸。主要用作驅動如車子，齒輪般動力機械。

### 產品參數

* 工作電壓：3.3V\~6V
* 額定電壓：4.8V
* 額定電流：200ma
* 堵轉電流：700ma
* 打滑電流：450ma
* 最大扭力：500g/cm(4.8V)
* 最高轉速：70rpm(3V供電情况下)
* 重量：12.4g
* 接口：紅黑線

### 使用注意事項

* 這只是一種小型電機，使用情境的扭力和電壓需求請不要過大。
* Geekservo電機沒有線序要求，調換線序只影響轉動方向。
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

將電機的紅黑線連接至Armourbit底部的電機接口。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/motor\_wire3.png)

```
沒有嚴格正負極之分，插的方向只會影響電機轉動方向。
```

#### RobotBit

將電機的紅黑線連接至RobotBit的電機接口。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/motorConRB.jpg)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/2kmotorConRB11.jpg)

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

電機積木塊

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
