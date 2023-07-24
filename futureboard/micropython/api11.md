# 未來板MicroPython編程11：RobotBit

### 導入未來板庫

需要先導入未來板的庫才可以使用未來板的硬件。

```
from future import *
```

### 11: RobotBit

### 導入RobotBit庫

```
import robotbit
```

#### 1. 初始化Robotbit擴展板

```
rb=robotbit.RobotBit()
```

#### 2. 控制電機

```
rb.motor(index,speed)
```

* index為電機序號，1\~4。
* speed代表速度，-255\~255。

#### 3. 停止所有電機

```
rb.motorStopAll()
```

#### 4. 控制180度舵機

```
rb.servo(index,degree)
```

* index可以填1\~8代表接口S1\~S8。 degree為角度，0\~180度。

#### 5. 控制GeekServo 9G舵機

```
rb.geekServo9g(index,degree)
```

* index可以填1\~8代表接口S1\~S8。
* degree為角度，-45\~225度。

#### 6. 控制GeekServo 2K舵機

```
rb.geekServo2kg(index,degree)
```

* index可以填1\~8代表接口S1\~S8。
* degree為角度，0\~360度。

#### 7. 轉動雙步進電機

```
rb.stepperDual(degree1,degree2)

degree1和degree2分別代表M1和M2。
```

#### 8. 轉動步進電機

```
rb.stepperDegree(index,degree)
```

* index為電機序號，1\~2。
* degree為角度。
