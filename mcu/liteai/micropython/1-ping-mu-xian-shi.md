# 1 屏幕顯示

### 1.1 全彩像素模式 <a href="#lczv2" id="lczv2"></a>

#### 1.1.1 構建對象

`class screen.Screen()`

```python
from screen import Screen()

screens = Screen()
screens.init()
```

**1.1.2 屏幕背光**

`setBrightness(state)`

參數

* state：int類型，0 關閉 / 1 開啟

#### 1.1.3 顯示方向

`setRotation(dir)`

參數

* state：int類型，0、90、180、270分別控制4個方向進行顯示

#### 1.1.4 自動刷新

`autoRefresh(switch)`

參數

* switch：bool類型，True 自動刷新 / False 關閉自動刷新

#### 1.1.5 刷新顯示

`refresh()`

#### 1.1.6 填充顯示

`fill(color)`

參數

* color：rgb

#### 1.1.7 清屏

`clear()`

#### 1.1.8 點亮像素

`pixel(x,y,color)`

參數

* x：int類型，橫向坐標，範圍0\~159
* y：int類型，縱向坐標，範圍0\~127
* color：rgb顏色

#### **1.1.9** 繪制線段

`line(x1,y1,x2,y2,color)`

參數

* x1：int類型，坐標1的橫坐標，範圍0\~159
* y1：int類型，坐標1的縱坐標，範圍0\~127
* x2：int類型，坐標2的橫坐標，範圍0\~159
* y2：int類型，坐標2的縱坐標，範圍0\~127
* color：rgb顏色

#### 1.1.10 繪制圓形

`circle(x,y,r,color)`

參數

* x：int類型，圓心橫向坐標，範圍0\~159
* y：int類型，圓心縱向坐標，範圍0\~127
* r：int類型，圓形半徑
* color：rgb顏色
* fill：bool類型，顏色是否填充圖形

#### 1.1.11 繪制三角形

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

#### 1.1.12 繪制多邊形

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

#### 1.1.13 顯示文本

`text(text,x,y,size,color)`

參數

* text：str類型，要顯示的文本
* x：int類型，中心橫坐標，範圍0\~159
* y：int類型，中心縱坐標，範圍0\~127
* size：int類型，字號(1-3)
* color：rgb顏色

#### 1.1.14 顯示多行文本

`smartText(text,x,y,color)`

* text：str類型，要顯示的文本，過長會自動分行
* x：int類型，中心橫坐標，範圍0\~159
* y：int類型，中心縱坐標，範圍0\~127
* color：rgb顏色
