# 智能節能路燈

智慧路燈是智慧城市中的重要組成部分，常見於馬路兩端。路燈本身用以照明，功能單一，而今現代尤其是一線城市中，一個簡單的路燈竟集成了物聯網控制，車流檢測，故障報警，遠程抄表，自動亮度調節等。本案例將實現其中的2點：物聯網控制與自動亮度調節。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/ex3.png)

### 搭建說明書與參考程式資源包:

[資源包下載](http://bit.ly/AIOTKit\_SH\_ResourcsePack)

### 參考接線:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/streetlamp\_wire.png)

### Micro:bit參考程式:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/streetlamp\_code\_1.87.png)

[參考程式下載](https://makecode.microbit.org/\_2p5gAx37q5KD)

### 加入插件:

IoT:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/iot.png)

### IoT參考程式:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/streetlamp\_iot\_code\_1.87.png)

### 啟動本地MQTT伺服器

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mqtt\_1.87.png)

### 程式流程

1. 將Micro:bit程式上載到Micro:bit。
2. 等待Wifibrick連上網絡。
3. 使用IoT程式，向街燈送出信號。1開燈，2關燈。
4. 燈的亮度會隨著環境亮度(Micro:bit亮度感測)的讀數轉變。
