from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
koi.setModel(256)
sleep(15)
koi.direction(2)
koi.mirror(0)
screen.sync = 0
while True:
  koi.read_from_uart()
  if sensor.btnValue('a'):
    koi.scanCodeSwitchType(0)
  if sensor.btnValue('b'):
    koi.scanCodeSwitchType(1)
  screen.fill((0, 0, 0))
  screen.text(koi.strVal,5,10,2,(255, 255, 255))
  screen.text(koi.xywh[0],5,40,1,(255, 255, 255))
  screen.text(koi.xywh[1],5,60,1,(255, 255, 255))
  screen.text(koi.xywh[2],5,80,1,(255, 255, 255))
  screen.text(koi.xywh[3],5,100,1,(255, 255, 255))
  screen.refresh()
