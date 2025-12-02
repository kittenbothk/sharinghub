from future import *
from sensor import Sensor
from koi2 import KOI2
from screen import Screen
from uwifi import WIFI
from agent import Agent
from fileOperations import *
animal = 0
screens = Screen()
sensors = Sensor()
wifipw = []
wifi = WIFI()
wifipw = (read_file('wifi.txt')).split(',')

wifi.connect(wifipw[0], wifipw[1])

expert = Agent("expert")
system_prompt = """
你是一個瀕危動物專家，你的職責是介紹小朋友提供的瀕危動物的資訊，例如但不限於: 特點，棲息地和瀕危的原因。回答盡量精簡，控制在90字之內。請以繁體中文回答。

"""

expert.add_prompt("system", system_prompt)
expert.clear()

koi = KOI2('uart0')
koi.direction(2)
koi.setModel(5)
koi.classifierLoad('/flash/'+'animals.json')
screens.autoRefresh(False)
animal = 'None'
ans = 'None'
def refresh():
  screens.fill((0, 0, 0))
  screens.text('瀕危物種AI圖鑑',5,10,1,(255, 255, 255))
  screens.text(animal,5,30,2,(0, 170, 0))
  screens.text(ans, 5, 55, 1, (0, 170, 0))
  screens.text('A:辨認',118,5,1,(255, 255, 255))
  screens.text('B:講解',118,20,1,(255, 255, 255))
  screens.text('M:查詢', 118, 35, 1, (255, 255, 255))
  screens.refresh()
while True:
  koi.read_from_uart()
  if sensors.btnValue('a'):
    animal = koi.strVal
    sleep(0.1)
  if sensors.btnValue('b'):
    if wifi.isconnect():
       ans = 'Asking AI'
       refresh()
       ans = expert.chat(animal)
       ans = ans.strip()
       refresh()
       expert.speak(ans)
    sleep(0.1)
  if sensors.btnValue('m'):
    if wifi.isconnect():
      ans = 'Listening'
      refresh()
      ans = expert.listen()
      refresh()
      ans = expert.chat(ans)
      ans = ans.strip()
      refresh()
      expert.speak(ans)
  refresh()
