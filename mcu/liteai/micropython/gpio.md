# 4 IO接口

## 4 IO接口

### 4.1 構建對象

`class future.MeowPin(pin,type)`

參數

* pin：str類型，引腳，可選參數
  * P1, P2, P3, P4
* type：str類型，設置引腳類型，可選參數：
  * IN：數字輸入
  * OUT：數字輸出
  * PWM：模擬輸出
  * ANALOG：模擬輸入

```python
from future import *

P1 = MeowPin('P1', 'IN')
```

### 4.2 設置引腳數字電平

`setDigital(level)`

參數

* level：int類型，輸出電平，0或1

### 4.3 獲取引腳數字電平

`getDigital()`

* 返回值：int類型，返回引腳電平

### 4.4 設置引腳模擬值

`setAnalog(value)`

參數

* value：int類型，輸出模擬值，範圍0\~4095

### 4.5 設置模擬輸出頻率

`setFrequency(hz)`

參數

* hz：int類型，頻率，範圍0\~122

### 4.6 讀取引腳模擬值

`getAnalog()`

* 返回值：int類型，範圍0\~4095
