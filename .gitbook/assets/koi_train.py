from future import *
from sensor import Sensor
from koi2 import KOI2
from screen import Screen

animals = []
index = 0
screens = Screen()
sensors = Sensor()


koi = KOI2('uart0')
koi.setModel(5)
koi.direction(2)
animals.clear()
animals.append('panda')
animals.append('cheetah')
animals.append('rhino')
animals.append('elephant')
animals.append('zebra')
index = 1
screens.autoRefresh(False)
while True:
  if sensors.btnValue('a'):
    koi.classifierAddTag(animals[int(index - 1)])
    sleep(0.1)
  if sensors.btnValue('b'):
    index += 1
    if index > len(animals):
      index = 1
    sleep(0.1)
  if sensors.btnValue('m'):
    koi.classifierSave('/flash/'+'animals.json')
    sleep(0.1)
  screens.fill((0, 0, 0))
  screens.text('Current Tag:',5,10,1,(255, 255, 255))
  screens.text((animals[int(index - 1)]),5,30,2,(0, 170, 0))
  screens.text('Press A to record',5,90,1,(255, 255, 255))
  screens.text('Press B for next tag',5,100,1,(255, 255, 255))
  screens.text('Press M to save',5,110,1,(255, 255, 255))
  screens.refresh()
