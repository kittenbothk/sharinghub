# 天氣小助手

可以檢測環境溫度和濕度，亦可以獲取天文台數據，出門之前用來查看天氣就最適合不過。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/weatherstation1.jpg)

### 組裝說明書

[組裝說明書下載](https://github.com/kittenbothk/kittenbothk/raw/master/Kits/future\_inventor/instructions/pdf/weatherstation.pdf)

### 參考接線

![](https://kittenbothk.readthedocs.io/en/latest/\_images/weatherstation\_wire.png)

### 參考程式

#### KittenBlock參考程式

![](https://kittenbothk.readthedocs.io/en/latest/\_images/weatherstation\_code.png)

[參考程式下載](https://github.com/kittenbothk/kittenbothk/raw/master/Kits/future\_inventor/instructions/sb3/weather.sb3)

#### Python參考程式

```
#/bin/python

from time import sleep
from future import *
from sugar import *
import robotbit
import urequests
import ujson
api_url='https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en'

x = 0

screen.sync = 1

robot = robotbit.RobotBit()

robot.geekServo2kg(1, 90)

wifi.connect(str("3DJollyFab"), "goodluckjf11b")

#init hko

screen.sync = 0

while True:
  r=urequests.get(api_url)
  weather=ujson.loads(r.content)
  
  screen.fill((0, 0, 0))
  screen.text(str("Temperature:"),5,10,1,(255, 255, 255))
  screen.text(str(str(ENV().update()[0])+str("C")),5,25,2,(255, 255, 255))
  screen.text(str("Humidity:"),5,50,1,(255, 255, 255))
  screen.text(str(str(ENV().update()[1])+str("%")),5,65,2,(255, 255, 255))
  screen.text(str("UV Index:"),5,90,1,(255, 255, 255))
  screen.text(str(weather['uvindex']['data'][0]['desc']),5,105,2,(255, 255, 255))
  screen.refresh()
  if weather['uvindex']['data'][0]['desc'] == "extreme":
    robot.geekServo2kg(1, 90)
  if weather['uvindex']['data'][0]['desc'] == "very high":
    robot.geekServo2kg(1, 220)
  if weather['uvindex']['data'][0]['desc'] == "high":
    robot.geekServo2kg(1, 150)
  if weather['uvindex']['data'][0]['desc'] == "moderate" or weather['uvindex']['data'][0]['desc'] == "low":
    robot.geekServo2kg(1, 330)
  sleep(5)
```

[參考程式下載](https://github.com/kittenbothk/kittenbothk/raw/master/Kits/future\_inventor/instructions/py/weather.py)

### 模型玩法

未來板會顯示當前溫度和濕度，左上方的指針會因應天氣指出相應的圖示，包括下雨或者紫外線指數。
