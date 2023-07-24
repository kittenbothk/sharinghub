# 工業4.0倉庫貨物管理系統未來板參考程式

### RFID讀取UUID程式

使用這程式查看RFID卡的UUID。

```
from time import sleep
from future import *
from sugar import *
def probeCallback():
  global x
    
  screen.fill((0, 0, 0))
  screen.text(str("Place RFID Tag"),5,10,1,(0, 119, 255))
  screen.text(str(RFID().uuid()),5,30,2,(0, 119, 255))
  screen.refresh()

x = 0

screen.sync = 0

screen.fill((0, 0, 0))

screen.text(str("Place RFID Tag"),5,10,1,(0, 119, 255))

screen.refresh()

sleep(1)

while True:
  RFID().probe(probeCallback if 'probeCallback' in dir() else None)
  sleep(0.2)
```

[參考程式](https://raw.githubusercontent.com/kittenbothk/kittenbothk/master/Kits/inventory\_system/py/uuid.py)

### RFID讀寫程式

使用這程式為RFID卡寫入數據。按A寫入，按B讀取。

```
from future import *
import sugar
from time import sleep

rfid = sugar.RFID()

while 1:
    if sensor.btnValue('a'):
        rfid.write(1, 1, 'ITEM')
        sleep(1)
    elif sensor.btnValue('b'):
        print(rfid.read(1, 1))
        sleep(1)
```

[參考程式](https://raw.githubusercontent.com/kittenbothk/kittenbothk/master/Kits/inventory\_system/py/RFID\_read\_write.py)

### MakerCloud參考程式

```
from future import *
from robotbit import RobotBit
from sugar import *
from time import sleep
from mqttsimple import MQTTClient

id=''
item=''
msg=''
mc_prefix='_dn=,_dsn=,'

koi_count=0
asr_count=0

def probeCallback():
    global koi_count
    global asr_count
    rb.motor(1,1)
    screen.clear()
    id=RFID().uuid()
    print(id)
    screen.text(id,5,40,2,(255,255,255))
    item=RFID().read(1, 1)
    print(item)
    screen.text(item,5,10,2,(255,255,255))
    msg=item+'.'+id
    print(mc_prefix+msg)
    makercloud.publish("",str(mc_prefix+'item='+msg))
    sleep(1)
    if (item=='koi'):
        koi_count+=1
        makercloud.publish("",mc_prefix+'koi_count='+str(koi_count))
    elif (item=='asr'):
        asr_count+=1
        makercloud.publish("",mc_prefix+'asr_count='+str(asr_count))
    rb.motor(1,-50)
    sleep(2)

rb=RobotBit()

wifi.connect('','')
sleep(3)
makercloud=MQTTClient("mqtt.makercloud.io", "clientID")
makercloud.connect()

makercloud.publish("",mc_prefix+'asr_count='+str(asr_count))
sleep(1)
makercloud.publish("",mc_prefix+'koi_count='+str(koi_count))

screen.clear()

while True:
    if sensor.btnValue('a'):
        rb.motor(1,-50)
    if sensor.btnValue('b'):
        rb.motor(1,0)
    RFID().probe(probeCallback if 'probeCallback' in dir() else None)
    sleep(0.2)
```

[參考程式](https://raw.githubusercontent.com/kittenbothk/kittenbothk/master/Kits/inventory\_system/py/conveyor\_belt.py)

#### 模型玩法

1. 在程式填入Wifi的登入資料和MakerCloud的主題資料
2. 在程式裡填入與貨品相應的RFID編號
3. 開啟電源後等待未來板連接到MakerCloud
4. 按A鍵啟動輸送帶，B鍵停止輸送帶
5. 當RFID魔塊感應到貨物的RFID晶片後，未來板會顯示RFID資訊，並且會將貨物資料上傳到MakerCloud平台
