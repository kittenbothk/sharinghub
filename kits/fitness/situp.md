# 2. 臥仰起坐測試

以超聲波測距檢測用戶完成臥仰起坐的次數，然後上傳至物聯網平台。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/pushup.png)

### 搭建說明書

[搭建說明書下載](https://github.com/kittenbothk/kittenbothk/raw/master/Kits/fitness/images/situp.pdf)

### 參考接線

#### 臥仰起坐

![](https://kittenbothk.readthedocs.io/en/latest/\_images/pushup\_wire.png)

### 參考程式

#### 臥仰起坐參考程式

{% embed url="https://makecode.microbit.org/_MpRaVHYYLKg7" %}

[臥仰起坐參考程式下載](https://makecode.microbit.org/\_MpRaVHYYLKg7)

### 使用方法

1. 將臥仰起坐的超聲波感應器固定在牆上，感應器的高度需要大約與用家頭部高度相若。
2. 開動Robotbit，等待WifiBrick連接到MakerCloud。
3. 當用戶做臥仰起坐時，需要將身體撐起，直至進入感應器的80cm範圍內，此時感應器會發出聲響並顯示剔號，示意用家已達到要求。
4. 然後需要將身體躺下，直至感應器發出聲響並顯示剔號，示意用家可以撐起身體繼續。
5. 按下A鍵查看完成掌上壓次數並上傳數據至物聯網。
6. 按下B鍵重置感應器，將次數歸0。
