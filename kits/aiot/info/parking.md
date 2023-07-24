# 無感支付停車場

所謂的無感支付就是藉助某物獨一無二的特徵，綁定相關支付工具後，通過對這種特徵的圖像掃描識別，從而自動快捷支付的方式。應用在停車場中，高速收費站等領域，通過識別車牌自動收費，大大降低了等待時間並提升工作效率。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/ex1.png)

### 搭建說明書與參考程式資源包:

[資源包下載](http://bit.ly/AIOTKit\_SH\_ResourcsePack)

### 參考接線:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/parking\_wire.png)

### 加入插件:

視訊偵測:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/video1.png)

百度大腦:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/baidu.png)

### 參考程式:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/parking\_code\_1.87.png)

### 程式流程

#### 這案例建議使用USB網絡攝像頭，將鏡頭放置在枱面上，逼真程度會比使用電腦內置攝像頭高。

1. 將Micro:bit連接到Kittenblock。**不需要將程式上載到Micro:bit。**
2. 按下1，辨認進入車輛之車牌號，並記錄進入時間。
3. 按下2，辨認離開車輛之車牌號，並記錄當前時間。
4. 程式顯示泊車時間並計算泊車費用。
