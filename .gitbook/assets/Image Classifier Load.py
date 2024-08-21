from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
koi.setModel(5)
sleep(15)
koi.direction(2)
koi.mirror(0)
screen.sync = 0
while True:
  koi.read_from_uart()
  if sensor.btnValue('a'):
    koi.classifierLoad('/flash/'+'abc.json')
    sleep(0.5)
  screen.fill((0, 0, 0))
  screen.text(koi.strVal,5,10,2,(255, 255, 255))
  screen.text(koi.getSimilarity(),5,40,2,(255, 255, 255))
  screen.refresh()
