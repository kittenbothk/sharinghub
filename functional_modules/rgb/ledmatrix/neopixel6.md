# 1616溢彩屏之動態效果教程

先前教程提及過，neomatrix的流水走字效果並不支援16x16的燈板。

本節教程將會教大家手動編寫16x16的流水效果。

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

### 流光溢彩屏進階Makecode編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner11.png)

1. 本節教程將會用到robotbit插件，請將插件加載於makecode。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/210.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/129.png)

1. 本節教程亦會用到neomatrix的編輯器。

#### [neomatrix編輯器](https://kittenbot.github.io/pxt-neomatrix/index.html)

請勿加載neomatrix插件！否則將會出現錯誤！ 只需要在瀏覽器打開編輯器即可。

#### 單幀流水動畫

**編程教學**

請先將燈板設置為矩陣。

```
有關矩陣的詳細教學可以參考《流光溢彩屏neopixel矩陣教程》。
```

[流光溢彩屏neopixel矩陣教程](neopixel2.md)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/code115.png)

```
注意：這裡我們設置變數strip改為rgb，這有助我們之後的操作。
```

接下來我們要添加一個函式。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/function1.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/function3.png)

現階段我們只需要將以下積木添加至我們剛剛做的函式和無限重複積木塊裏。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/code210.png)

接下來我們轉到neomatrix的編輯器。 在編輯器繪畫我們想要的圖畫。

完成之後我們要在Input中按Makecode JS。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/editor12.png)

生成Javascript編碼之後我們將rgb.clear()至到rgb.show()之內的程式複製。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/editor21.png)

在makecode之中我們需要按JavaScript切換至JavaScript模式。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/editor31.png)

現在我們找出我們剛才做的函式。

然後將剛才複製的程式在strip.clear()和basic.pause()中間貼上。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/js2.png)

之後我們需要手動檢查Y的數值以修正X。假如Y的數值為雙數，我們要用矩陣闊度與X相減。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/js1.png)

```
電腦由0開始計算，所以我們需要用15來修正X。
用PowerBrick套件中的全彩點陣屏的話不需要更改。
```

修正所有數值之後就可以進行下一步。

在變數欄中增加2項變數，用來控制燈板動畫。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/editor41.png)

```
注意：因為X的方向會左右相反，我們必須2項變數，1項為順序(position)，另1項為倒序(reversepos)。
這教程是想控制圖畫的左右移動，如欲做到上下移動，請參考本教程自行修改程式。
```

完成後我們在程式增加以下積木。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/code34.png)

我們切換至JavaScript模式，手動檢查Y的數值。假如Y為單數，我們在X加上position +，否則我們加上reversepos +。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/js3.png)

修正所有數值之後就大功告成了！

![](https://kittenbothk.readthedocs.io/en/latest/\_images/1frame1.gif)

[參考程式](https://bit.ly/LEDMatrixT4\_01Hex)

[參考程式網址](https://makecode.microbit.org/\_dtwYPt8zvXEp)

#### 雙幀流水動畫

上文教了大家創作地單一幅幀數的動畫，有了這個基礎，我們製作多幀動畫時就較容易上手。

**編程教學**

我們會沿用上部分已完成的程式。我們先到neomatrix編輯器生成第二幅圖畫。

生成之後將JavaScript程式碼貼在第一幀後。 按照上部分手動更改X的數值。

為第二幀圖畫增添一個抵銷(offset)。Y為單數的時候要-15，否則+15。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/js4.png)

```
增加了offset，第二幀圖畫會在彩屏外的範圍出現，隨著位置的轉變，圖畫會走入彩屏範圍裏。
抵銷的數值為燈板闊度並因幀數調節，這裡添加了一幀，所以我們加減15(15x1=15)。
```

切換至積木模式，更改動畫重置的臨界點。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/code42.png)

```
臨界點數值和重置位置可能因應圖畫而轉變。
這裡設置臨界點為24，重置點為-8，代表動畫重置前移動32格(2幀圖畫的總闊度)。
假如你想較早重置，您可以將臨界點調低，反之亦然。
一般而言，重置點都會設在0以下，這可以避免動畫突然重置到畫面上。
```

大功告成！

![](https://kittenbothk.readthedocs.io/en/latest/\_images/2frame1.gif)

[參考程式](https://bit.ly/LEDMatrixT4\_02Hex)

[參考程式網址](https://makecode.microbit.org/\_AxqhpeafJ8jv)

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
