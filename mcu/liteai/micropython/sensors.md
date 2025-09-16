# 2 板載感應器

## 2.1 按鍵

### 2.1.1 構建對象

`class sensor.Sensor()`

```python
from sensor import Sensor

sensors = Sensor()
```

### 2.1.2 檢測按下

`btnValue(btn=None)`

參數

* btn：str類型，'a' 按鍵A / 'm' 按鍵M / 'b' 按鍵M

返回值：

* 提供參數：bool類型，True 按下 / False 未按下；
* 不提供參數：list類型，返回按下的按鍵，如A和B同時按下返回 \['a', 'b']

## 2.2 光線強度

### 2.2.1 構建對象

`class sensor.Sensor()`

```python
from sensor import Sensor()

sensors = Sensor()
```

### 2.2.2 亮度數值

`getLight()`

* 返回值：int類型，範圍0\~4096

## 2.3 運行時間

`time.monotonic()`

* 返回值：double類型，主板運行時間

## 2.4 CPU溫度

`cpu.temperature`

* 返回值，double類型，cpu溫度

```python
from microcontroller import cpu
print(cpu.temperature)
```

## 2.5 加速度計

### 2.5.1 構建對象

`class sensor.Da213()`

```python
from sensor import Da213

acc = Da213()
```

### 2.5.2 加速度

`accX()`

`accY()`

`accZ()`

* 返回值-2\~2

### 2.5.3 主板姿態

`gesture(posture)`

參數

* posture：str類型

```
shake：搖晃
freefall：自由落體
tilt_up：正立
tilt_down：倒立
tilt_left：左傾
tilt_right：右傾
face_up：屏幕朝上
face_down：屏幕朝下
```

* 返回值：bool類型，與傳入參數姿態對應時返回true

### **2.5.4** 姿態角

俯仰角：`pitch()`

翻滚角：`roll()`

* 返回值：double類型，返回對應的姿態角度
