# SugarBox整合氣象站

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### 模型搭建說明書

{% file src="../../../../.gitbook/assets/weatherstation_building instructions.pdf" %}

### 模型接線圖

<figure><img src="../../../../.gitbook/assets/weatherstation_building instructions 33.png" alt=""><figcaption></figcaption></figure>

### MakeCode參考程式

{% hint style="info" %}
風向的數值需校正。
{% endhint %}

{% embed url="https://makecode.microbit.org/_Pk8Vrq62KX7i" %}

#### 模型玩法

1. 可以按A和B切換多種模式，相關的數據會在OLED上顯示。
   1. 模式1:  風向與風速模式
   2. 模式2: 溫度與氣壓模式
   3. 模式3: 亮度與雨量模式
2. 說出Check Temperature或Check Humidity，語音模組會報讀溫度或濕度
