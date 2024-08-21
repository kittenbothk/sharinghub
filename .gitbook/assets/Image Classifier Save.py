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
    koi.classifierAddTag('A')
    sleep(0.2)
  if sensor.btnValue('b'):
    koi.classifierAddTag('B')
    sleep(0.2)
  if koi.getBtnState('A'):
    koi.classifierSave('/flash/'+'abc.json')
