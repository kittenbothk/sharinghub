from future import *
from INA226 import *
from screen import Screen

v = 0
ma = 0
ina226 = INA226()
screens = Screen()


screens.init()
screens.autoRefresh(False)
while True:
  v = ina226.bus_voltage_v
  ma = ina226.current_ma
  screens.fill((0, 0, 0))
  screens.text('導電性測試',50,5,1,(255, 255, 255))
  screens.text(('電壓:'+str(v)),5,20,1,(255, 0, 0))
  screens.text(('電流:'+str(ma)),85,20,1,(0, 170, 0))
  if v < 0.01:
    screens.text('閉合電路:',5,40,1,(170, 0, 0))
    screens.text('斷路',70,40,2,(170, 0, 0))
  else:
    screens.text('閉合電路:',5,40,1,(0, 170, 0))
    screens.text('通路',70,40,2,(0, 170, 0))
    if ma < 0.1:
      screens.text('不是導電物料',5,80,2,(170, 0, 0))
    else:
      screens.text('是導電物料',5,80,2,(0, 170, 0))
  screens.refresh()
