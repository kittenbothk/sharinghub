# 未來板MicroPython編程3：蜂鳴器

### 導入未來板庫

需要先導入未來板的庫才可以使用未來板的硬件。

```
from future import *
```

### 03: 蜂鳴器類

#### 1. 蜂鳴器頻率發聲

```
buzzer.tone(freq,d=0.5)
```

使用頻率控制蜂鳴器。

freq為頻率，頻率與音調對照表可以參考： [https://pages.mtu.edu/\~suits/notefreqs.html](https://pages.mtu.edu/~suits/notefreqs.html)

d為持續時間(秒)，預設為0.5秒，d=-1時會持續發聲。

#### 2. 蜂鳴器根據音符發聲

```
buzzer.note(note,beats=1)
```

note為音調，0\~130，總共12個8度，12的倍數為該8度的C音。

beats為持續拍數，預設為1。

#### 3. 蜂鳴器休止

```
buzzer.rest(beats=1)
```

beats為持續拍數，預設為1。

#### 4. 蜂鳴器設置bpm

```
buzzer.bpm(bpm=120)
```

bpm為拍速，預設為120。

#### 5. 蜂鳴器停止

```
buzzer.stop()
```

#### 6. 蜂鳴器播放旋律

```
buzzer.melody(m)
```

m為旋律，可以使用內建旋律或自訂旋律。

內建旋律:

```
CORRECT = "c6:1 f6:2 "
NOTICE = "d5:1 b4:1 "
ERROR = "a3:2 r a3:2 "
DADA = "r4:2 g g g eb:8 r:2 f f f d:8 "
ENTERTAINER = "d4:1 d# e c5:2 e4:1 c5:2 e4:1 c5:3 c:1 d d# e c d e:2 b4:1 d5:2 c:4 "
PRELUDE = "c4:1 e g c5 e g4 c5 e c4 e g c5 e g4 c5 e c4 d g d5 f g4 d5 f c4 d g d5 f g4 d5 f b3 d4 g d5 f g4 d5 f b3 d4 g d5 f g4 d5 f c4 e g c5 e g4 c5 e c4 e g c5 e g4 c5 e "
ODE = "e4 e f g g f e d c c d e e:6 d:2 d:8 e:4 e f g g f e d c c d e d:6 c:2 c:8 "
NYAN = "f#5:2 g# c#:1 d#:2 b4:1 d5:1 c# b4:2 b c#5 d d:1 c# b4:1 c#5:1 d# f# g# d# f# c# d b4 c#5 b4 d#5:2 f# g#:1 d# f# c# d# b4 d5 d# d c# b4 c#5 d:2 b4:1 c#5 d# f# c# d c# b4 c#5:2 b4 c#5 b4 f#:1 g# b:2 f#:1 g# b c#5 d# b4 e5 d# e f# b4:2 b f#:1 g# b f# e5 d# c# b4 f# d# e f# b:2 f#:1 g# b:2 f#:1 g# b b c#5 d# b4 f# g# f# b:2 b:1 a# b f# g# b e5 d# e f# b4:2 c#5 "
RING = "c4:1 d e:2 g d:1 e f:2 a e:1 f g:2 b c5:4 "
FUNK = "c2:2 c d# c:1 f:2 c:1 f:2 f# g c c g c:1 f#:2 c:1 f#:2 f d# "
BLUES = "c2:2 e g a a# a g e c2:2 e g a a# a g e f a c3 d d# d c a2 c2:2 e g a a# a g e g b d3 f f2 a c3 d# c2:2 e g e g f e d "
BIRTHDAY = "c4:3 c:1 d:4 c:4 f e:8 c:3 c:1 d:4 c:4 g f:8 c:3 c:1 c5:4 a4 f e d a#:3 a#:1 a:4 f g f:8 "
WEDDING = "c4:4 f:3 f:1 f:8 c:4 g:3 e:1 f:8 c:4 f:3 a:1 c5:4 a4:3 f:1 f:4 e:3 f:1 g:8 "
FUNERAL = "c3:4 c:3 c:1 c:4 d#:3 d:1 d:3 c:1 c:3 b2:1 c3:4 "
PUNCHLINE = "c4:3 g3:1 f# g g#:3 g r b c4 "
BADDY = "c3:3 r d:2 d# r c r f#:8 "
CHASE = "a4:1 b c5 b4 a:2 r a:1 b c5 b4 a:2 r a:2 e5 d# e f e d# e b4:1 c5 d c b4:2 r b:1 c5 d c b4:2 r b:2 e5 d# e f e d# e "
BA_DING = "b5:1 e6:3 "
WAWA = "e3:3 r:1 d#:3 r:1 d:4 r:1 c#:8 "
JUMP_UP = "c5:1 d e f g "
JUMP_DOWN = "g5:1 f e d c "
POWER_UP = "g4:1 c5 e g:2 e:1 g:3 "
POWER_DOWN = "g5:1 d# c g4:2 b:1 c5:3 "
```

自訂旋律:

* 以c4:2為例子：
  * C代表音調
  * 4代表八度
  * :2代表持續時間

[Next ](https://kittenbothk.readthedocs.io/en/latest/futureboard/micropython/api4.html)[ Previous](https://kittenbothk.readthedocs.io/en/latest/futureboard/micropython/api2.html)<br>
