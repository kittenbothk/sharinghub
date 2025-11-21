# 未來版MicroPython編程7：WiFi與物聯網

### 導入未來板庫

需要先導入未來板的庫才可以使用未來板的硬件。

```
from future import *
```

### 07: WiFi與物聯網

#### 1. 連接WiFi

```
wifi.connect('router','password')
```

填寫WiFi網絡的登入資料，注意未來版只能連上2.4GHz的網絡。

#### 2. 獲取網絡狀態

```
wifi.sta.isconnected()
```

成功連接網絡返回1，否則返回0。

#### 3. 獲取網絡資料

```
wifi.sta.ifconfig()
```

返回一個列表，獲取連接中網絡的資訊。

列表內容：IP地址，網絡遮罩，閘道，域名。

#### 4. 獲取MAC地址

```
import machine
import ubinascii

x = ubinascii.hexlify(machine.unique_id()).decode().upper()
```

取得未來版的獨特實體地址。

#### 5. 檔案下載

```
wifi.download("url","name")
```

下載檔案到SD卡，url為檔案網網址，name為檔案名稱。

#### 1\~4使用範例

```
#/bin/python
from future import *

from time import sleep

import machine
import ubinascii

wifi.connect(str("name"), "pwd")
sleep(5)
if wifi.sta.isconnected():
  screen.clear()
  screen.text(str("IP: ")+str(wifi.sta.ifconfig()[0]),5,10,1,(0, 119, 255))
  screen.text("MAC Address: ",5,25,1,(0, 119, 255))
  screen.text(ubinascii.hexlify(machine.unique_id()).decode().upper(),5,35,1,(0, 119, 255))
  screen.text("Subnet Mask: ",5,50,1,(0, 119, 255))
  screen.text(wifi.sta.ifconfig()[1],5,60,1,(0, 119, 255))
  screen.text(str("Gateway: ")+str(wifi.sta.ifconfig()[2]),5,75,1,(0, 119, 255))
  screen.text(str("DNS: ")+str(wifi.sta.ifconfig()[3]),5,90,1,(0, 119, 255))
```

### 導入MQTT庫

```
import mqttsimple
```

使用MQTT與相關的功能前必須要導入MQTT庫。

#### 5. 初始化MQTT

```
myMQTT = mqttsimple.MQTTClient(server,client_id,port=0,user=None,password=None,keepalive=0,ssl=False,ssl_params={})
```

這裡需要建立一個MQTTclient class的object，不是直接呼叫函數。

一般用家只需要注意server,client\_id。

server為伺服器的地址，client\_id為用戶名稱(一般可以任意填寫)。

假如你的伺服器需要登入，請在user和password裏填入登入資料。

#### 6. 連接MQTT伺服器

```
myMQTT.connect()
```

#### 7. 切斷MQTT連接

```
myMQTT.disconnect()
```

#### 8. 訂閱MQTT話題

```
myMQTT.subscribe(topic=)
```

在topic填入話題的名稱。

#### 9. 發佈信息到MQTT話題

```
myMQTT.publish(topic,msg)
```

在topic填入話題，msg填入訊息。

#### 10. 讀取MQTT話題訊息

```
myMQTT.mqttRead(topic)
```

在topic填入話題的名稱。

#### 11. 獲取已訂閱話題最後一則訊息

```
myMQTT.check_msg()
```

#### 12. 等待直到已訂閱話題收到訊息

```
myMQTT.wait_msg()
```

#### 13. 設定MQTT讀取訊息觸發函數

```
def myFunction(topic,msg):
    print(topic)
    print(msg)

myMQTT.set_callback(myFunction())
```

#### MQTT範例程序1：使用返回值獲取信息

```
import mqttsimple
if not(wifi.sta.isconnected()):
    wifi.connect('router', 'password') 

c = mqttsimple.MQTTClient("myServer", 'myID')
c.connect() 

c.subscribe('/topic1')

x= 0
# mqttRead()會不斷讀取訊息，假如話題沒有新的信息則會返回None。
while 1:
    if sensor.btnValue('a'):
        x+=1
        c.publish('/topic1','x'+str(x))
        sleep(0.2)
    # 假如讀取的訊息不是None，就顯示訊息。
    mqttT = c.mqttRead('/topic1')
    if mqttT:
        print(mqttT)
```

#### MQTT範例程序2：使用函數觸發使用MQTT

```
import mqttsimple
if not(wifi.sta.isconnected()):
    wifi.connect('router', 'password') 

c = mqttsimple.MQTTClient("myServer", 'myID')
c.connect() 

# 設置觸發函數，假如話題有信息更新就會自動觸發
def sub_cb(topic, msg):
    print((topic, msg))   
c.set_callback(sub_cb)
    
c.subscribe('/ttt')

while 1:
    if sensor.btnValue('a'):
        c.publish('/ttt', 'hello')
        sleep(0.2)
    # 獲取已訂閱話題最後一則訊息
    c.check_msg()

# 你亦可以試試等待直到已訂閱話題收到訊息
# c.wait_msg()
```

[Next ](https://kittenbothk.readthedocs.io/en/latest/futureboard/micropython/api8.html)[ Previous](https://kittenbothk.readthedocs.io/en/latest/futureboard/micropython/api6.html)<br>
