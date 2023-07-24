# 流光溢彩屏之Neopixel矩陣教程

## 流光溢彩屏之Neopixel矩陣教程

本節教程將會介紹流光溢彩屏的矩陣操作。矩陣可以幫我們做一些比較複雜的圖形。

### 接線

0832溢彩屏需要配合robotbit使用，請按照下圖將屏幕與robotbit接線。

#### 1. 將彩屏與轉接板連接。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/matrixtoadapter.jpg)

#### 2. 將轉接板連接到robotbit。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/adaptertorobotbit.png)

#### 3. 長時間使用請使用USB供電。

USB供電時，不需要使用Robotbit供電，請將5V電源線拔走。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/usb1.jpg)

#### 4. 完整接線示範

![](https://kittenbothk.readthedocs.io/en/latest/\_images/usbpower.jpg)

### 流光溢彩屏與矩陣

![](https://kittenbothk.readthedocs.io/en/latest/\_images/Matris.png)

矩陣(matrix)可以理解為一個有X和Y軸的表格，例如一個有10個列和10個欄的表格可以被稱之為一個10x10的矩陣。

以電腦屏幕為例，大家口中的1920x1080其實就等於一個1920x1080的矩陣了。

換而言之，我們現在手上的流光溢彩屏都可以矩陣來表達為8x32或者16x16的矩陣。透過矩陣，我們就可以做更多不同的效果。

### Makecode編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner11.png)

#### 此節教程將會運用neopixel插件，請將插件加載。

我們先來試試初始燈板為一個16x16的矩陣。然後我們可以透過X和Y座標控制個別圖元。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/code82.png)

```
這裡使用的是一塊16x16燈板，所以我們將闊度設為16。
```

[參考程式下載](https://bit.ly/LEDMatrixT3\_01Hex)

[參考程式網址](https://makecode.microbit.org/\_WWiYHp7F50Cg)

現在我們來試試點亮首2行的第一顆圖元。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/code44.png)

[參考程式下載](https://bit.ly/LEDMatrixT3\_02Hex)

[參考程式網址](https://makecode.microbit.org/\_T02XMz8ooihy)

大家可以看到雖然在Y為0和1這兩行上；

我們均點亮X為0的圖元時，2行中被點亮圖元卻不一樣。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/ww.jpg)

這是因為燈板是一條蛇狀的燈條所摺成的，所以X的方向會因Y軸而改變。（請參考下圖）

![](https://kittenbothk.readthedocs.io/en/latest/\_images/asd.png)

以圖中最上2行為例，在第一行(Y為0)中X的方向是由右至左；

在第二行(Y為1)中X的方向卻變成由左至右了。

因應這個情況，我們需要當在Y為單數的時候，將X的方向手動調轉。

```
電腦由0開始計算，所以第一行的Y其實是0，第二行才是1。
```

調轉的方法十分簡單，只需要用矩陣的闊度減去X就可以了。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/code52.png)

[參考程式下載](https://bit.ly/LEDMatrixT3\_03Hex)

[參考程式網址](https://makecode.microbit.org/\_bjMWtxVJpffc)

```
雖然矩陣的闊度為16但由於電腦以0開始計算，我們需要減去1。（16-1=15）
用PowerBrick套件中的全彩點陣屏的話不需要更改。
```

![](https://kittenbothk.readthedocs.io/en/latest/\_images/www.jpg)

所以，當我們想用燈板顯示一些圖案的時候，我們必須因應Y軸而改變X。

#### 使用矩陣顯示圖案示範

![](https://kittenbothk.readthedocs.io/en/latest/\_images/code72.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/triangle.jpg)

[參考程式下載](https://bit.ly/LEDMatrixT3\_04Hex)

[參考程式網址](https://makecode.microbit.org/\_5Fiag7F001ec)

### 流光溢彩屏矩陣旋轉

我們可以在這程式中看到旋轉對於X和Y軸的影響。

有時候我們把燈板的方向旋轉會方便我們的操作。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/code117.png)

```
由於旋轉方向有0、1、2這3種，我們使用除以3的餘數操控旋轉。
```

![](https://kittenbothk.readthedocs.io/en/latest/\_images/rotate.gif)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/rotate32.gif)

[參考程式下載](https://bit.ly/LEDMatrixT3\_05Hex)

[參考程式網址](https://makecode.microbit.org/\_E95HhRdT5gPX)

X和Y軸的方向可以參照下圖。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/image8554.png)

### 插件版本與更新

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../../../makecode/makecodeextupdate.md)

### FAQ

問：為什麼我點亮燈板的時候，燈板未能顯示我定下的顏色，燈板只點亮了紅色？

答：電源不足夠。

解決方法：將robotbit的電源打開，或者在供電轉接板加插外部USB電源。

### 注意事項

* 請勿接駁電壓高於5V的電源。
* 長時間使用請接駁USB外部電源。
* 要點亮大量LED的時候請將亮度減低。
* 本產品只適合14歲以上的兒童獨立使用，8-14歲兒童請在成年人的陪同下使用。
* 使用前請參考Kittenbot官方資料，不要隨便接駁電路，請勿外接大電流電機舵機。
* 請勿在金屬表面或導電性物料上使用，以免短路。
* 請勿在有水或潮濕的地方使用，以免短路。
* 請勿用手觸碰燈板外露的電線。
