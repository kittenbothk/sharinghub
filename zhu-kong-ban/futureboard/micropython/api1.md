# 未來板MicroPython編程1：屏幕

可以在這裡找到未來板的MicroPython編程的教學。

### 導入未來板庫

需要先導入未來板的庫才可以使用未來板的硬件。

```
from future import *
```

### 01：屏幕類

#### 1. 屏幕填充

```
screen.fill(color)
```

color參數為顏色，有3種用法：

1. RGB數值，0～255。例如(255,100,0)。
2. 明度，0\~255。例如100。
3. 內置顏色，包括RED、YELLOW、PINK、WHITE、GREEN、BLUE、PURPLE、CYAN、BLACK。

#### 2. 繪製像素點

```
screen.pixel(x,y,color)
```

x，y參數為座標，分別為0\~159和0\~127。

color參數為顏色，有3種用法：

1. RGB數值，0～255。例如(255,100,0)。
2. 明度，0\~255。例如100。
3. 內置顏色，包括RED、YELLOW、PINK、WHITE、GREEN、BLUE、PURPLE、CYAN、BLACK。

#### 3. 繪製線條

```
screen.line(x1,y1,x2,y2,color)
```

x1，y1，x2，y2參數為座標，x和y分別為0\~159和0\~127。x1，y1和x2，y2分別指線條的兩端。

color參數為顏色，有3種用法：

1. RGB數值，0～255。例如(255,100,0)。
2. 明度，0\~255。例如100。
3. 內置顏色，包括RED、YELLOW、PINK、WHITE、GREEN、BLUE、PURPLE、CYAN、BLACK。

#### 1\~3使用範例：

```
from future import *

screen.fill(BLACK)
screen.pixel(80,62,(200,200,0))
screen.pixel(80,64,(200,200,0))
screen.pixel(80,66,(200,200,0))
screen.line(30,30,90,90,255)
```

***

#### 4. 繪製矩形

```
screen.rect(x,y,w,h,color,fill)
```

x，y參數為座標，分別為0\~159和0\~127。座標為矩形的左上角。

w和h分別為闊和長。

color參數為顏色，有3種用法：

1. RGB數值，0～255。例如(255,100,0)。
2. 明度，0\~255。例如100。
3. 內置顏色，包括RED、YELLOW、PINK、WHITE、GREEN、BLUE、PURPLE、CYAN、BLACK。

fill為填充參數，1代表填充，0代表不填充。默認為0。

#### 5. 繪製圓形

```
screen.circle(x,y,r,color,fill)
```

x，y參數為座標，分別為0\~159和0\~127。座標為圓形的圓心。

r為半徑。

color參數為顏色，有3種用法：

1. RGB數值，0～255。例如(255,100,0)。
2. 明度，0\~255。例如100。
3. 內置顏色，包括RED、YELLOW、PINK、WHITE、GREEN、BLUE、PURPLE、CYAN、BLACK。

fill為填充參數，1代表填充，0代表不填充。默認為0。

#### 6. 繪製三角形

```
screen.triangle(x1,y1,x2,y2,x3,y3,color,fill)
```

x1，y1，x2，y2，x3，y3參數為座標，x和y分別為0\~159和0\~127。x1，y1、x2，y2和x3，y3分別指三角形的三個角。

color參數為顏色，有3種用法：

1. RGB數值，0～255。例如(255,100,0)。
2. 明度，0\~255。例如100。
3. 內置顏色，包括RED、YELLOW、PINK、WHITE、GREEN、BLUE、PURPLE、CYAN、BLACK。

fill為填充參數，1代表填充，0代表不填充。默認為0。

#### 7. 繪製多邊形

```
screen.polygon(x,y,sides,r,th,rot,color,fill)
```

x，y參數為座標，分別為0\~159和0\~127。座標為多邊形的中心點。

sides參數代表邊的數量，不能低於3。

r參數代表圖形的半徑。

th代表邊的粗幼，默認為3。

rot代表圖形的旋轉，默認為0。

color參數為顏色，有3種用法：

1. RGB數值，0～255。例如(255,100,0)。
2. 明度，0\~255。例如100。
3. 內置顏色，包括RED、YELLOW、PINK、WHITE、GREEN、BLUE、PURPLE、CYAN、BLACK。

fill為填充參數，1代表填充，0代表不填充。默認為0。

#### 4\~7使用範例

```
from future import *

screen.fill((0, 0, 0))
screen.rect(5,5,50,20,(0, 119, 255),1)
screen.circle(50,50,20,(170, 0, 0),0)
screen.triangle(10,50,60,100,10,100,(0, 170, 0),0)
screen.polygon(120,50,5,30,3,0,(255, 255, 0),1)
```

***

#### 8. 顯示英文字串

```
screen.text(text, x=0, y=0, ext=1, color=255)
```

x，y參數為座標，分別為0\~159和0\~127。座標為文字的左上角。

ext參數為文字大小，默認為1=8x8像素。

color參數為顏色，有3種用法：

1. RGB數值，0～255。例如(255,100,0)。
2. 明度，0\~255。例如100。
3. 內置顏色，包括RED、YELLOW、PINK、WHITE、GREEN、BLUE、PURPLE、CYAN、BLACK。

#### 9. 顯示中文字串

```
screen.textCh(text, x=0, y=0, ext=1, color=255)
```

x，y參數為座標，分別為0\~159和0\~127。座標為文字的左上角。

ext參數為文字大小，默認為1=12x12像素。

color參數為顏色，有3種用法：

1. RGB數值，0～255。例如(255,100,0)。
2. 明度，0\~255。例如100。
3. 內置顏色，包括RED、YELLOW、PINK、WHITE、GREEN、BLUE、PURPLE、CYAN、BLACK。

#### 8\~9 使用範例

```
from future import *

screen.text('hello world',5,5,1,RED)
screen.textCh('你好',5,25,2,WHITE)
```

***

#### 10. 顯示圖片

```
screen.loadBmp(path, x=0, y=0)
screen.loadPng(path, x=0, y=0)
screen.loadGif(path, x=0, y=0)
```

x，y參數為座標，分別為0\~159和0\~127。座標為圖片的左上角。

#### 10 使用範例

```
# 顯示png
from future import *
screen.loadPng('hmP.png')

# 顯示gif
from future import *
while 1:
    screen.loadgif('hmG.gif')
```

#### 11. 屏幕同步刷新

```
screen.sync = val
```

val參數為狀態，0=關閉，1=開啟。默認為開啟。

#### 12. 屏幕刷新

```
screen.refresh()
```

#### 11\~12 使用範例

```
# 關閉屏幕刷新可以消除閃屏
from future import *
x=0
while True:
  screen.fill((0, 0, 0))
  screen.circle(x,50,10,(0, 255, 0),1)
  screen.refresh()
  x += 1
```
