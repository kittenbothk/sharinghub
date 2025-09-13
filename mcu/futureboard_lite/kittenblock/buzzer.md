# 蜂鳴器

<figure><img src="../../../.gitbook/assets/image (15) (1).png" alt=""><figcaption></figcaption></figure>

通過pwm和系統時間達成不同的音調與節拍從而封裝而成的蜂鳴器音樂庫

### 參考程式1: 自定義旋律

{% hint style="info" %}
生日快樂：c4:4 c4:4 d4:4 c4:4 f4:4 e4:8 r:4 c4:4 c4:4 d4:4 c4:4 g4:4 f4:8 r:4 c4:4 c4:4 c5:4 a4:4 f4:4 e4:4 d4:8 r:4 bb4:4 bb4:4 a4:4 f4:4 g4:4 f4:8

● 以c4:2為例子：\
○ c：英式命名法，代表音調，分別對應著do\~xi，一個八度大致分為cdefab這7個調子。\
○ 4：八度，比如4，為第四八度\
○ :2：持續時間，以bpm=120且四分音符為一拍的默認情況下，1秒2拍=>0.5秒/拍，2則代表著4分音符的一半，所以該c4:2的時長持續為0.25s
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (16) (1).png" alt=""><figcaption></figcaption></figure>

### 參考程式2:持續播放和休止

<figure><img src="../../../.gitbook/assets/image (17).png" alt="" width="262"><figcaption></figcaption></figure>

### 參考程式3:播放指定旋律

<figure><img src="../../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>
