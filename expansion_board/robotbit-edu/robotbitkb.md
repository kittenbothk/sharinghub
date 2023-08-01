# Robotbit Edu在Kittenblock編程

Robotbit Edu在Kittenblock編程

Robotbit Edu亦支援在Kittenblock上編程。

有關Kittenblock的介紹可以參考：[Kittenblock大全](../../ge-bian-cheng-ping-tai-jie-shao/kittenblock/)

### 這教學會使用Micro:bit V1或V2作例子，有關未來板或Meowbit的Robotbit Edu使用教學請參考相關的教學。

[未來板Robotbit Edu使用教學](../../zhu-kong-ban/futureboard/kittenblock/robotbit.md)

Meowbit Robotbit Edu使用教學

### Kittenblock編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbbanner4.png)

首先將Microbit用USB線連接到電腦。

在左上角小貓logo旁邊的硬件欄選擇硬件，加載Robotbit的插件。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/add5.png)

在Microbit的積木欄中按下感嘆號 ( ! ) 按鈕。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbmbcon4.png)

然後點選『開始連線』。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbmbcon12.png)

連接完成！

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbmbcon22.png)

成功連接後，MicroBit會顯示心形。

假如沒有顯示心形，可以按下升級韌體。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/upload5.png)

#### 加載成功

![](https://kittenbothk.readthedocs.io/en/latest/\_images/success1.png)

#### 1. 電機編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/robotbit\_motorKB1.png)

Kittenbot每款電機的詳細教學可以參考：電機教學

示範接線與編程：

將電機連接在Robotbit Edu的M1A和M1B上。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/motor\_wire1.png)

```
電機速度範圍由-255至255
```

![](https://kittenbothk.readthedocs.io/en/latest/\_images/motor\_code\_kb1.png)

#### 2. 舵機編程

Kittenbot每款舵機的詳細教學可以參考：舵機教學

示範接線與編程：

將舵機連接在Robotbit Edu的S1上。

```
將舵機的橙色線接到黃色引腳針線，紅色線接到紅色正極針線，黑色線接到黑色負極針線。
```

![](https://kittenbothk.readthedocs.io/en/latest/\_images/servo\_wire1.png)

```
由於舵機轉動需要時間，所以我們需要加一個短暫的停頓(pause)，給予舵機足夠時間轉動。
一般舵機的轉向角度範圍由0至180度
```

![](https://kittenbothk.readthedocs.io/en/latest/\_images/servo\_code\_kb1.png)

#### 3. 步進電機編程

Kittenbot每款電機的詳細教學可以參考：電機教學

示範接線與編程：

將步進電機連接到Robotbit Edu的M1和M2上（將紅色電線連接到VM）。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/stepper\_wire1.png)

```
步進電機的角度範圍為-360至360度
```

![](https://kittenbothk.readthedocs.io/en/latest/\_images/stepper\_code\_kb1.png)

#### 4. RGB燈編程

```
所有積木都需要加一個”顯示”的積木才會顯示效果。
```

**4.1 點亮RGB燈**

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kb\_code51.png)

**4.2 使用RGB數值指定顏色**

```
RGB的數值範圍由0-255。
```

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kb\_code61.png)

**4.3 點亮指定一顆燈**

```
只適合於燈條。
```

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kb\_code71.png)

#### 5. 引腳編程

引腳的讀寫需要用到Microbit的積木塊。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/robobit\_pinKB4.png)

```
Pin 0-2可以用作類比引腳，其他Pin只可以用作數位引腳。
類比數值範圍由0-1023，數位數值範圍由0至1。
```

![](https://kittenbothk.readthedocs.io/en/latest/\_images/robobit\_pinKB11.png)

**5.1 引腳數值讀取**

```
Pin 0預設與蜂鳴器相接，所以使用Pin 0引腳時需要拔除跳線帽。
```

![](https://kittenbothk.readthedocs.io/en/latest/\_images/robobit\_pinKB21.png)

**5.2 引腳數值寫入**

```
Pin 0預設與蜂鳴器相接，所以使用Pin 0引腳時需要拔除跳線帽。
```

![](https://kittenbothk.readthedocs.io/en/latest/\_images/robobit\_pinKB31.png)
