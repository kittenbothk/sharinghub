# 本地簡易氣象站

氣象站是物聯網的基礎，主要是將檢測到的本地數據通過網絡上傳到雲端，從物聯網平臺監測氣象。當然一般的氣象站都帶顯示功能，介於我們手頭沒有顯示器件，就用舵機與平台來顯示數據。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/ex5-1.png)

### 搭建說明書與參考程式資源包:

[資源包下載](http://bit.ly/AIOTKit\_SH\_ResourcsePack)

### 參考接線:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/weatherstation\_wire\_1.87.png)

### Micro:bit參考程式:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/weatherstation\_code\_1.87.png)

### 加入插件:

[參考程式下載](https://makecode.microbit.org/\_3gqKev0WHCmW)

IoT:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/iot.png)

### IoT參考程式:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/weatherstation\_iot\_code\_1.87.png)

### 啟動本地MQTT伺服器

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mqtt\_1.87.png)

### 程式流程

1. 將Micro:bit程式上載到Micro:bit。
2. 等待Wifibrick連上網絡。
3. 氣象站會在儀表上匯報當時氣溫與相對濕度。
4. IoT程式的小貓會說出氣象站探測到的氣溫與相對濕度。
