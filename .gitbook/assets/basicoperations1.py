from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
while True:
  koi.read_from_uart()
  if sensor.btnValue('a'):
    koi.displayText(0+40,0,3*1000,(255, 255, 255),'hello')
  if koi.getBtnState('A'):
    koi.takePic('/flash/'+'abc.jpg')
  if koi.getBtnState('B'):
    koi.displayPic('/flash/'+'abc.jpg',3*1000)
