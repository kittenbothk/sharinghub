# 未來板MicroPython編程4：海龜繪圖

### 導入未來板庫

需要先導入未來板的庫才可以使用未來板的硬件。

```
from future import *
```

### 04: 海龜繪圖類

#### 1. 設置海龜顏色

```
turtle.fillcolor(color)
```

color為RGB數值，0～255。例如(255,100,0)。

#### 2. 海龜前進

```
turtle.forward(steps)
```

steps為前進步數。

#### 3. 海龜左轉／右轉

```
turtle.left(angle)
turtle.right(angle)
```

angle為角度。

#### 4. 海龜設定向前角度

```
turtle.setheading(angle)
```

angle為角度。

#### 5. 海龜移動到某一點

```
turtle.goto(x,y)
```

x，y參數為座標，分別為0\~159和0\~127。

#### 6. 海龜設定座標

```
turtle.setx(x)
turtle.sety(y)
```

x，y參數為座標，分別為0\~159和0\~127。

#### 7. 海龜繪畫點

```
turtle.dot(d)
```

d參數為直徑。

#### 8. 海龜繪畫圓圈

```
turtle.circle(r,angle)
```

r參數為半徑。angle參數為角度，360為之一個完整的圓圈。

#### 9. 海龜設定填充

```
turtle.begin_fill()
turtle.end_fill()

#注意：由於未來板的硬件像素未達到海龜之需求，使用填充可能會有bug，無法正常填充。
```

#### 10. 海龜落筆抬筆

```
turtle.pendown()
turtle.penup()
```

#### 11. 海龜清屏

```
turtle.clear()
```

#### 海龜使用範例

```
from future import *

turtle.clear()
turtle.penup()
turtle.setx(80)
turtle.sety(64)
turtle.pendown()
for i in range(5):
    turtle.forward(40)
    turtle.right(144)
```

[Next ](https://kittenbothk.readthedocs.io/en/latest/futureboard/micropython/api5.html)[ Previous](https://kittenbothk.readthedocs.io/en/latest/futureboard/micropython/api3.html)\
