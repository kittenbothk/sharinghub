# 無按鈕電梯說明書

在抗疫期間，大家都會盡量避免觸摸公用物件，以免沾上病毒。有見及此，這案例模擬了一台非接觸式升降機，讓乘客不用觸摸按鈕也可以使用升降機。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/lift1.png)

### 教材資源包下載

包括說明書： [資源包下載地址](https://bit.ly/AIHealthCareSetBuildingGuide)

### 參考接線

![](https://kittenbothk.readthedocs.io/en/latest/\_images/liftcon.png)

### 參考程式

#### 訓練程序

{% embed url="https://makecode.microbit.org/_3EMDjb05rKCu" %}

[參考程式](https://makecode.microbit.org/\_3EMDjb05rKCu)

#### 無按鈕電梯

{% embed url="https://makecode.microbit.org/_2RmRD3Eo16oR" %}

[參考程式](https://makecode.microbit.org/\_2RmRD3Eo16oR)

### 模型玩法

#### 首先載入訓練程序

1. 打開電源後，等待10秒讓KOI完全開機。
2. 做出G樓的手勢，對準鏡頭然後按下B按鍵，重複大約3次然後按下A按鍵完成訓練。
3. 使用同樣方法訓練1樓和2樓的手勢。
4. 最後走出鏡頭範圍，對背景進行訓練。
5. 完成所有訓練之後同時按下A和B按鍵，儲存訓練的檔案。

#### 然後載入升降機程序

1. 打開電源後，等待10秒讓KOI完全開機。
2. 按下B按鍵，模型會開始辨識手勢。
3. 對鏡頭做出相應手勢，升降機就會移動到相應樓層。
