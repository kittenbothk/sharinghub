from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
koi.setModel(3)
sleep(15)
koi.initCustomModel(10616832,[1.25,1.25,1.50,1.50,1.72,1.72,1.97,1.97,2.34,2.31])
koi.direction(2)
koi.mirror(0)
screen.sync = 0
while True:
  koi.read_from_uart()
  screen.fill((0, 0, 0))
  screen.text(koi.numberVal,5,10,2,(255, 255, 255))
  screen.text(koi.xywh[0],5,30,2,(255, 255, 255))
  screen.text(koi.xywh[1],5,50,2,(255, 255, 255))
  screen.text(koi.xywh[2],5,70,2,(255, 255, 255))
  screen.text(koi.xywh[3],5,90,2,(255, 255, 255))
  screen.refresh()
