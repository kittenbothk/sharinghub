---
description: 2KG電機 (HKBD8009A)
---

# GeekServo 2KG電機

![](https://kittenbothk.readthedocs.io/en/latest/\_images/image--0101.png)

這是一款兼容樂高插孔的高扭力的電機，相對於9g電機，在同等供電下具有更高轉速。輸出軸為兩組樂高十字孔，主要用在驅動動力機械。

### 產品參數

* 工作電壓：3.3V\~6V
* 額定電壓：4.8V
* 額定電流：70mA
* 堵轉電流：900mA
* 打滑電流：700mA
* 最大扭力：1.6kg±0.2kg/cm(4.8V)
* 最高轉速：120rpm(3V供電情况下)
* 重量：20g
* 接口：紅黑線

### 產品特色：

![](https://kittenbothk.readthedocs.io/en/latest/\_images/2kg\_1.jpg)

繼承了GeekServo 9G舵機電機的優點，增強了扭力與速度，改善了結構

* 採用十字沉孔作輸出軸
  * 可以因使用情況自由插入不同長度的十字軸
* 扭力更大
  * 扭力為GeekMotor 9G的三倍左右

### 規格尺寸

#### 樂高孔單位:

* 長度：5孔
* 闊度：3孔
* 高度：3孔
* 輸出軸：樂高十字軸

#### mm單位:

* 長度：40mm
* 闊度：24mm
* 高度：24mm
* 輸出軸：樂高十字軸

![](https://kittenbothk.readthedocs.io/en/latest/\_images/0111.png)

### 接線方法

#### Armourbit

將電機的紅黑線連接至Armourbit底部的電機接口。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/2kmotorCon.jpg)

```
沒有嚴格正負極之分，插的方向只會影響電機轉動方向。
```

#### Robotbit

將電機的紅黑線連接至RobotBit的電機接口。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/2kmotorConRB.jpg)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/2kmotorConRB11.jpg)

```
沒有嚴格正負極之分，插的方向只會影響電機轉動方向。
```

### MakeCode編程教學

#### 此模組可供Microbit和Meowbit使用。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner17.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/acbanner3.png)

#### Armourbit

#### 加載Powerbrick插件：

#### 在擴展頁直接搜尋Powerbrick (powerbrick已經過微軟認證，可以直接搜尋)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/powerbrick\_search2.png)

#### [詳細方法](../programmingplatforms/makecode/kittenbotandmakecode.md)

#### 電機積木塊:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/2kmotorblocks.png)

#### 電機編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/2kmotorcode.png)

[參考程式網址](https://makecode.microbit.org/\_RYHivyayYL4q)

#### RobotBit

#### 加載RobotBit插件：

![](https://kittenbothk.readthedocs.io/en/latest/\_images/robotbitExtension.png)

#### [詳細方法](../programmingplatforms/makecode/kittenbotandmakecode.md)

#### 電機積木塊:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/2kmotorblocks\_rb1.png)

#### 電機編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/2kmotorcode\_rb1.png)

[參考程式網址](https://makecode.microbit.org/\_33HMywgx9H97q)

#### Meowbit:

#### 加載robotbit插件：https://github.com/KittenBot/meow-robotbit

#### [詳細方法](https://kittenbothk.readthedocs.io/en/latest/Makecode/powerBrickMC.html)

#### 電機積木塊:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/motorblocks2.png)

### 電機編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/2kmotorcode\_meow1.png)

[參考程式網址](https://makecode.com/\_2z0C8v6XAC5y)

### 插件版本與更新

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../programmingplatforms/makecode/makecodeextupdate.md)

### KittenBlock編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbbanner12.png)

#### 這教學使用Microbit作例子，每款擴展板/主控板的使用教學請參考相應頁面。

#### Armourbit

#### 加載PowerBrick插件

在左上角小貓logo旁邊的硬件欄選擇PowerBrick，加載Microbit與Powerbrick插件。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/addextension4.png)

#### 電機積木塊

![](https://kittenbothk.readthedocs.io/en/latest/\_images/2kkbmotorblocks.png)

#### 電機編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/9gmotor\_armourbit\_kb\_code1.png)

[參考程式下載](https://bit.ly/PowerbrickM11\_01sb3)

#### Robotbit

#### 加載Robotbit插件

在左上角小貓logo旁邊的硬件欄選擇Microbit，加載Microbit與Robotbit插件。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/addRB3.png)

#### 電機積木塊

![](https://kittenbothk.readthedocs.io/en/latest/\_images/rbmotorblocks.png)

#### 電機編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/9gmotor\_robotbit\_kb\_code1.png)

### FAQ

1：為什麼我點擊積木塊沒有反應呢？

首先確保已經連接好Microbit，然後上載韌體再試一試。
