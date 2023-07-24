# 智能化健身啞鈴

所謂智能化就是將原本人為操作的事情用某種方式轉變為機器來代工。對於智能化健身器械來說，有如健身單車，通過使用它會將健身時間和卡路里消耗數據顯示在屏幕上，免去了人為計算的功夫，甚至更準確。健身啞鈴可以記錄抬舉的次數，上傳到雲端讓每天的健身數據得以可視化，概念性提倡鍛煉身體的重要性。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/ex10.png)

### 搭建說明書與參考程式資源包:

[資源包下載](http://bit.ly/AIOTKit\_SH\_ResourcsePack)

### 參考接線:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/dumbbell\_wire.png)

### 加入插件:

IoT:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/iot.png)

### Micro:bit參考程式:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/dumbbell\_code\_1.87.png)

### IoT參考程式:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/dumbbell\_iot\_code\_1.87.png)

### 啟動本地MQTT伺服器

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mqtt\_1.87.png)

### 程式流程

1. 將Micro:bit程式上載到Micro:bit。
2. 等待Wifibrick連上網絡。
3. 使用啞鈴舉重。完成健身後按A，將訓練數據送上伺服器。
4. IoT程式的小貓會說出訓練數據。
