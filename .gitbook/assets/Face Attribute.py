from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
koi.setModel(9)
sleep(15)
koi.direction(2)
koi.mirror(0)
screen.sync = 0
while True:
  koi.read_from_uart()
  screen.fill((0, 0, 0))
  screen.text(int(koi.getFaceAttr(4)),5,10,1,(255, 255, 255))
  screen.text(koi.xywh[0],5,30,1,(255, 255, 255))
  screen.text(koi.xywh[1],5,50,1,(255, 255, 255))
  screen.text(koi.xywh[2],5,70,1,(255, 255, 255))
  screen.text(koi.xywh[3],5,90,1,(255, 255, 255))
  screen.refresh()
