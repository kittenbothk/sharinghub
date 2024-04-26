# 口罩佩戴偵測器說明書

在抗疫期間，佩戴口罩成為市民大眾的習慣，不同場所也規定要佩戴口罩才可入內。這個案例模擬了口罩檢測閘門，只許有口罩的人士進入。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/maskdoor1.png)

### 教材資源包下載

包括說明書： [資源包下載地址](https://bit.ly/AIHealthCareSetBuildingGuide)

### 參考接線

![](https://kittenbothk.readthedocs.io/en/latest/\_images/maskdoorcon.png)

### 參考程式

#### 模型訓練程式

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mask\_train\_code.png)

{% embed url="https://makecode.microbit.org/_Hj67sX8xhCvt" %}

#### 口罩辨認程式

{% embed url="https://makecode.microbit.org/_93vXqc757UKc" %}

[口罩佩戴偵測器參考程式](https://makecode.microbit.org/\_93vXqc757UKc)

### 模型玩法

#### 模型訓練程式

1. 打開電源後，等待10秒讓KOI完全開機。
2. 戴上口罩，將鏡頭準自己然後按下A按鍵進行訓練，重複大約3次。
3. 除下口罩，將鏡頭準自己然後按下B按鍵進行訓練，重複大約3次。
4. 按下KOI的A按鍵，對背景進行訓練。
5. 同時按下Microbit的A和B鍵，將模型儲存到SD卡上。

#### 口罩辨認程式

1. 打開電源後，等待10秒讓KOI完全開機。
2. 按下Microbit的A按鍵，KOI偵測到戴上口罩的人臉時，大閘會打開。
