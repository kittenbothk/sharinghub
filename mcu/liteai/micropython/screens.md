# 1 屏幕顯示

## 1.1 全彩像素模式 <a href="#lczv2" id="lczv2"></a>

### 1.1.1 構建對象

`class screen.Screen()`

```python
from screen import Screen()

screens = Screen()
screens.init()
```

### **1.1.2 屏幕背光**

`setBrightness(state)`

參數

* state：int類型，0 關閉 / 1 開啟

### 1.1.3 顯示方向

`setRotation(dir)`

參數

* state：int類型，0、90、180、270分別控制4個方向進行顯示

### 1.1.4 自動刷新

`autoRefresh(switch)`

參數

* switch：bool類型，True 自動刷新 / False 關閉自動刷新

### 1.1.5 刷新顯示

`refresh()`

### 1.1.6 填充顯示

`fill(color)`

參數

* color：rgb

### 1.1.7 清屏

`clear()`

### 1.1.8 點亮像素

`pixel(x,y,color)`

參數

* x：int類型，橫向坐標，範圍0\~159
* y：int類型，縱向坐標，範圍0\~127
* color：rgb顏色

### **1.1.9** 繪制線段

`line(x1,y1,x2,y2,color)`

參數

* x1：int類型，坐標1的橫坐標，範圍0\~159
* y1：int類型，坐標1的縱坐標，範圍0\~127
* x2：int類型，坐標2的橫坐標，範圍0\~159
* y2：int類型，坐標2的縱坐標，範圍0\~127
* color：rgb顏色

### 1.1.10 繪制圓形

`circle(x,y,r,color)`

參數

* x：int類型，圓心橫向坐標，範圍0\~159
* y：int類型，圓心縱向坐標，範圍0\~127
* r：int類型，圓形半徑
* color：rgb顏色
* fill：bool類型，顏色是否填充圖形

### 1.1.11 繪制三角形

`triangle(x1,y1,x2,y2,x3,y3,color,fill)`

參數

* x1：int類型，坐標1的橫坐標，範圍0\~159
* y1：int類型，坐標1的縱坐標，範圍0\~127
* x2：int類型，坐標2的橫坐標，範圍0\~159
* y2：int類型，坐標2的縱坐標，範圍0\~127
* x3：int類型，坐標2的橫坐標，範圍0\~159
* y3：int類型，坐標2的縱坐標，範圍0\~127
* color：rgb顏色
* fill：bool類型，顏色是否填充圖形

### 1.1.12 繪制多邊形

`polygon(x,y,rim,diameter,thickness,skewing,color,fill)`

參數

* x：int類型，橫向坐標，範圍0\~159
* y：int類型，縱向坐標，範圍0\~127
* rim：int類型，設置邊的數量
* diameter：int類型，直徑
* thickness：int類型，厚度
* skewing：int類型，旋轉，以中心公轉偏移
* color：rgb顏色
* fill：bool類型，顏色是否填充圖形

```python
from future import *
from screen import Screen


screens = Screen()


screens.autoRefresh(False)
screens.fill((0, 0, 0))
screens.polygon(50,50,5,50,3,0,(0, 170, 170),0)
screens.refresh()
```

### 1.1.13 顯示文本

`text(text,x,y,size,color)`

參數

* text：str類型，要顯示的文本
* x：int類型，中心橫坐標，範圍0\~159
* y：int類型，中心縱坐標，範圍0\~127
* size：int類型，字號(1-3)
* color：rgb顏色

### 1.1.14 顯示多行文本

`smartText(text,x,y,color)`

參數

* text：str類型，要顯示的文本，過長會自動分行
* x：int類型，中心橫坐標，範圍0\~159
* y：int類型，中心縱坐標，範圍0\~127
* color：rgb顏色

### 1.1.15 顯示圖片

`loadimg(path,x,y)`

參數

* path：str類型，圖片路徑
* x：int類型，中心橫坐標，範圍0\~159
* y：int類型，中心縱坐標，範圍0\~127

## 1.2 點陣模式

### 1.2.1 構建對象

`class future.Matrix()`

```python
from future import *

matrix = Matrix()
```

### 1.2.2 點陣比例

`init(x,y)`

參數

* x：int類型，橫坐標的像素數量
* y：int類型，縱坐標的像素數量

### **1.2.3 显示图标**

`show(t)`

參數

* t：list類型，0 滅 / 1 亮

<pre class="language-python"><code class="lang-python"><strong>#示例——显示爱心
</strong><strong>from future import *
</strong>
matrix = Matrix()
matrix.show([0,1,0,1,0,1,0,1,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0])
</code></pre>

### 1.2.4 顯示字符

{% hint style="info" %}
僅支持5x5和8x8的點陣模式
{% endhint %}

`scroll(text)`

參數

* text，str類型，要顯示的文本

### 1.2.5 點亮像素

`pix(x,y,light)`

參數

* x：int類型，橫坐標，範圍0\~4
* y：int類型，縱坐標，範圍0\~4
* light：int類型，亮度，範圍0\~255

## 1.3 海龜繪圖

### 1.3.1 構建對象

`class turtle.Turtle()`

```python
from future import *
from turtle import Turtle

turtles = Turtle()
```

### 1.3.2 畫筆顏色

`fillcolor(color)`

參數

* color：rgb顏色

### 1.3.3 擡筆

`penup()`

### 1.3.4 落筆

`pendown()`

### 1.3.5 前進

`forward(distance)`

參數

* distance：int類型，想要移動的像素

### 1.3.6 左轉

`left(angle)`

參數

* angle：int類型，旋轉角度

### 1.3.7 右轉

`right(angle)`

參數

* angle：int類型，旋轉角度

### 1.3.8 朝向

`setheading(angle)`

參數

* angle：int類型，旋轉角度

### 1.3.9 移動到坐標

`goto(x,y)`

參數

* x：int類型，中心橫坐標，範圍0\~159
* y：int類型，中心縱坐標，範圍0\~127

### 1.3.10 設置x坐標

`setx(x)`

參數

* x：int類型，中心橫坐標，範圍0\~159

### 1.3.11 設置y坐標

`sety(y)`

參數

* y：int類型，中心縱坐標，範圍0\~127

### 1.3.12 繪制弧度

`circle(r,angle)`

參數

* r：int類型，半徑
* angle，int類型，角度

### **1.3.13** 畫點

`dot(size)`

參數

* size：int類型，點大小

### 1.3.14 開始填充&結束填充

`begin_fill()`

`end_fill()`

```python
from future import *
from turtle import Turtle

turtles = Turtle()

turtles.clear()
turtles.penup()
turtles.goto(50, 50)
turtles.pendown()
turtles.begin_fill()
turtles.setheading(90)
turtles.forward(20)
turtles.right(90)
turtles.forward(20)
turtles.right(90)
turtles.forward(20)
turtles.right(90)
turtles.forward(20)
turtles.end_fill()

```
