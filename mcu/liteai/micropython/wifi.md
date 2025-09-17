# 10 WIFI

## 10 WIFI

### 10.1 構建對象

`class uwifi.WIFI()`

```python
from uwifi import WIFI

wifi = WIFI()
```

### 10.2 連接wifi

`connect(ssid,pwd)`

參數

* ssid：str類型，wifi名
* pwd：str類型，wifi密碼

### 10.3 wifi連接狀態

`isconnect()`

* 返回值：bool類型，連接成功返回true

### 10.4 wifi信息

`Configuration()`

* 返回值：元組 (ip, 子掩碼, 網關, dns)

### 10.5 斷開連接

`disconnect()`

### 10.6 連接mqtt

`mqttConnect(url,id,user,pwd)`

參數

* url：str類型，mqtt服務器地址
* id：str類型，客戶端id（自定義）

### 10.7 訂閱話題

`subscribe(topic)`

參數

* topic：str類型，話題名稱

### 10.8 讀取話題消息

`getMessage(topic)`

參數

* topic：str類型，話題名稱

### 10.9 發送話題消息

`publish(topic,message)`

參數

* topic：str類型，話題名稱
* message：str類型，消息內容

### 10.10 初始化ntp時間

`initNTP(tz_offset,server)`

參數

* tz\_offset：int類型，時區
* server：str類型，ntp服務器地址

### 10.11 獲取時間

`getNTPtime(type)`

參數

* type：str類型
  * year
  * mon
  * wday
  * hour
  * min
  * sec
  * yday
