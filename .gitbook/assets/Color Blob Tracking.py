from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
koi.setModel(16)
screen.sync = 0
while True:
  koi.read_from_uart()
  if sensor.btnValue('a'):
    koi.colorSwitch(0)
  if sensor.btnValue('b'):
    koi.colorCalibration()
    koi.colorSwitch(9)
  screen.fill((0, 0, 0))
  screen.text(koi.xywh[0],5,10,1,(255, 255, 255))
  screen.text(koi.xywh[1],5,30,1,(255, 255, 255))
  screen.text(koi.xywh[2],5,50,1,(255, 255, 255))
  screen.text(koi.xywh[3],5,70,1,(255, 255, 255))
  screen.refresh()
