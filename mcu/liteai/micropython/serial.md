# 9 串口

## 9 串口

### 9.1 構建對象

`uart.Uart(port,baud)`

參數

* port：str類型
  * uart0, uart1
* baud：int類型

```python
from future import Uart

uart0 = Uart('uart0',115200)
```

### 9.2 檢查串口是否有數據

`existData()`

* 返回值：bool類型，串口有數據時候返回true

### 9.3 讀取所有串口數據

`readAll()`

* 返回值：byte

### 9.4 讀取一行串口數據

`readLine()`

* 返回值：byte

### 9.5 讀取指定長度的數據

`readLen()`

* 返回值：byte

### 9.6 寫入數據

`writeText(data,line)`

參數

* data：str類型
* line：bool類型，True時換行

### 9.7 寫入字節

`writeByte(bytes)`

參數

* bytes：字節組
