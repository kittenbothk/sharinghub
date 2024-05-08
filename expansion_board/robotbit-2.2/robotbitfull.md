---
description: Robotbit擴展板(HKBK8001A)
---

# Robotbit 介紹

### 產品名稱：

**Robotbit (Version 2.2)**

適用於校本中小學生編程教育 / 培訓機構 / 編程愛好者

_需配套Microbit進行使用_

### 配送清單

* RobotbitV2.2 X1
* Robotbit 專用底座
*   優質18650 鋰電池 X 1 (選購)

    ![](https://kittenbothk.readthedocs.io/en/latest/\_images/Robotbit\_18650.png)

### 產品特色

*   具有強大的驅動能力，支援直流電機 (DC motor) x 4、步進電機 (Stepper motor) x 2、舵機 (Servo Motor) x 8。

    [動力示範](https://youtu.be/jVWFA1n4N74)
* 將Microbit空閑引腳全部引出，支援大部份arduino以及市面上的常見電子模塊。
*   簡化供電要求, 統一供電到所有輸出位置，電源穏定

    自帶18650電池座，可選以鋰電池供電到板上所有輸出位置 (方便之選);

    亦可選擇以外部電源輸入方式，以電池盒供電 (提升動力之選; 最高可輸入6V電壓,即4粒1.5V 3A/2A電池)
*   Robotbit 專用底座: 保護之餘, 還提供標準樂高孔, 跟樂高積本無縫接軌。

    ![](<../../.gitbook/assets/Robotbit V2.2+P.png>)

    [底座安裝示範](https://youtu.be/FhimDxoAsj4)
* 板載蜂鳴器，為micro:bit 發聲。
* 前置4粒可獨立編程 RGB LED, 為項目增加光元素。

Robotbit示範短片

{% embed url="https://youtu.be/4tjt9Iy68sY" %}

### 外觀規格

* 產品尺寸：78mm x 57mm x 23mm
* PCB板厚 ： 1.5mm
* 小孔直徑 ： 3.0mm
* 大孔直徑 ： 4.8mm
* 凈重（不含包裝）:37.5g

![](https://kittenbothk.readthedocs.io/en/latest/\_images/robotbitSize.png)

### 功能規格

* 18650電池電壓：3.7V
* USB輸入電壓：5V
* VM引腳最大：1A（在板載電池的支持下）
* 綠色端子電壓(外部電源輸入)：5V（最大支持6V輸入，切勿接超6V的電壓，最大電流支持3A）

### 接口介紹

![](https://kittenbothk.readthedocs.io/en/latest/\_images/02\_1.png)

1. USB外部5V電源端子
2. 電源開關
3. 電源指示燈
4. 電量指示燈
5. MicroUSB 鋰電池充電口
6. 4路直流馬逹 (DC Motor) / 2路28BYJ步進馬逹 (Stepper Motor)
7. 蜂鳴器 (Buzzer) 跳線帽
8. 8路IO(對應Micro：bit P0-P2、P8、P12-P15)
9. 5V輸出與GND排針
10. 無源蜂鳴器 (Buzzer)
11. 8路舵機 (Servo Motor) 3PIN接口
12. I2C接口(可拓展I2C模塊)
13. 18650鋰電池座
14. 電池保護激活按鈕
15. Microbit插槽
16. 全彩RGB LED x 4

![](https://kittenbothk.readthedocs.io/en/latest/\_images/03\_1.png)

1. 舵機驅動芯片
2. 電機驅動芯片
3. 標準KittenBot機器人底盤固定孔
4. 標準樂高孔

### Robotbit各個部分詳解

![](https://kittenbothk.readthedocs.io/en/latest/\_images/48.png)

#### 18650電池座

#### ![../../\_images/09\_1.png](https://kittenbothk.readthedocs.io/en/latest/\_images/09\_1.png)

收到擴展板首先安裝18650鋰電池，注意電池正負極，切勿裝反！

當第一次安裝電池時，擴展板處於待激活狀態（電源燈不亮），此時需要短按一下電池保護激活按鈕或連接USB供電，使拓展板進入正常工作模式。 （如果你重新安裝電池，就需要操作這個步驟）

#### 18650電源開關

![](https://kittenbothk.readthedocs.io/en/latest/\_images/116.png)

開關打開後（撥向綠色端子那邊為打開開關），為Micro:bit和擴展板的接口供電。（擴展板需要裝上18650電池）

#### Micro USB 鋰電池充電口

![](https://kittenbothk.readthedocs.io/en/latest/\_images/103.png)

電腦供電或任意5V 1A或者1A以上的手機充電器均可為18650鋰電池充電。5V1A的充電器約2.5小時充滿，建議充電時關閉電源。充滿會自動截止，指示燈變綠。**充滿電後請把USB 拔走, 不宜長充, 同時請細閱讀盒內附帶之”鋰電池使用貼士”。**

```
attention: 只能用於充電, 不是用於下載hex程式
```

#### 電源與電量指示燈

![](https://kittenbothk.readthedocs.io/en/latest/\_images/123.png)

Led（3）為電源指示燈，打開開關後常亮Led（1）為充電指示燈，充電過程中常亮，電量充滿後Led（2）常亮

#### Micro:bit立式插槽

![](https://kittenbothk.readthedocs.io/en/latest/\_images/133.png)

用於安裝Microbit主板。

安裝方向：Micro:bit帶按鍵一面（正面）朝向Robotbit 上的 4顆LED方向。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/001\_01.png)

如若不慎反插, 只需拔出重新按正確方向插入便可; Micro:bit / Robotbit 不會因反插而損壞 。

#### 4路全彩RGB燈

![](https://kittenbothk.readthedocs.io/en/latest/\_images/143.png)

4路RGB燈實際與Micro:bit的P16相連控制

#### 8路舵機標準3Pin接口

![](https://kittenbothk.readthedocs.io/en/latest/\_images/191.png)

*   8路舵機實際通過專門的舵機擴展驅動芯片與Micro:bit的I2C口控制,而非IO口控制。

    ```
    attention: 舵機接口不能作為普通IO口使用, 只能驅動舵機 
    ```
* 擴展板在18650電池狀態下，最多能支持8個9g舵機（總電流<2A），禁止使用MG995等大電流舵機，以免燒壞擴展板 。
*   擴展板在外部電源接口（綠色端子）供電狀態下（5V 3A或者3A以上），最多能支持總電流不超過3A的舵機。

    ![](https://kittenbothk.readthedocs.io/en/latest/\_images/robotbit\_extPower.png)

#### DC motor 直流電機 x 4 或 Stepper Motor 步進電機 (28BYJ ) x 2

![](https://kittenbothk.readthedocs.io/en/latest/\_images/171.png)

在隨香港代理選購的電池下工作，一共可以同時控制4個（左右兩側合計）TT馬達，或者2個步進電機（與舵機合計總電流＜2A），禁止接大電流DC 馬逹和大電流步進馬逹 (建議選配Kittenbot的馬逹) ，以免燒毀擴展板 。

支持直流電機與步進電機混合使用（2個直流電機與1個步進電機）（與舵機合計總電流<2A）

#### 蜂鳴器與跳帽 (Jumper)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/21\_1.png)

* 蜂鳴器跳帽於出廠時默認已插上，把蜂鳴器與Micro:bit的P0口連接
* 如果想正常使用P0口的IO口讀寫功能，需要把蜂鳴器跳帽拔下來
* 蜂鳴器硬件上的電氣連接與Microbit的Music積木塊是對應的，可直接使用Music控制蜂鳴器。

#### Micro:bit的IO口引出

![](https://kittenbothk.readthedocs.io/en/latest/\_images/181.png)

已經將Micro:bit上P0-P2、P8、P12-P15轉出到擴展板上(P0使用時需要拔掉跳帽)標準的arduino 3PIN接口，支持市面上的Arduino模塊與常用模塊。P0-P2支持數字讀寫和模擬類比(Analogue)，P8、P12-P15只支持數位(Digital)讀寫。如果需要使用5V輸出模塊，可以接3PIN接口左側的5V電源。(3PIN接口的電源默認是3.3V)

#### I2C接口

![](https://kittenbothk.readthedocs.io/en/latest/\_images/191.png)

可拓展I2C模塊，只能用於插接I2C模塊，不能用於普通IO口讀寫

#### 2PIN外接電源端子

![](https://kittenbothk.readthedocs.io/en/latest/\_images/20.png)

* 雖然有防反接功能，但接線仍需要註意正負極。
* 外接線端子支持DC 5V的外部電源供電，推薦5V 2A以上電源供電以滿足拓展板驅動高扭矩舵機的電流需求。
* 內部電源供電時，舵機VM接口電源為18650電池電壓3.7V；當使用外部電源供電時，舵機VM接口的電壓為5V 負載電流最大3A。

### Robotbit新手必看快速入門教程

#### 把18650電池裝到Robotbit上，注意正負極

#### ![../../\_images/z1.gif](https://kittenbothk.readthedocs.io/en/latest/\_images/z1.gif)

#### 把Microbit插到Robotbit上，注意插接方向

#### ![../../\_images/z4.gif](https://kittenbothk.readthedocs.io/en/latest/\_images/z4.gif)

#### 點擊電池激活按鈕

#### ![../../\_images/z2.gif](https://kittenbothk.readthedocs.io/en/latest/\_images/z2.gif)

#### 打開18650電池開關

#### ![../../\_images/z3.gif](https://kittenbothk.readthedocs.io/en/latest/\_images/z3.gif)

### 軟件支援

配套硬件：Microbit

編程平台：Kittenblock(基於Scratch3.0) / Microsoft Makecode / Python(Mu editor)

#### Microsoft MakeCode

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner5.png)

#### ![../../\_images/04\_1.png](https://kittenbothk.readthedocs.io/en/latest/\_images/04\_1.png)

**1. 在makecode添加包中直接搜索Robotbit（Robotbit插件已經通過微軟官方認證)**

![](https://kittenbothk.readthedocs.io/en/latest/\_images/38\_01.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/39\_1.png)

**2. 在Kittenbot makecode離線版本中，添加包列表可以顯示Robotbit以及其他集成擴展包（Robotbit可以離線加載不依靠網絡，其他的擴展包不可以）**

**加載成功**

![](https://kittenbothk.readthedocs.io/en/latest/\_images/success.png)

#### KittenBlock（Kittenbot 圖形化編程軟件 基於Scratch 3.0）

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbbanner3.png)

**1. 打開Kittenblock, 把microbit 插到電腦USB port後, 按下圖次序點選**

![](https://kittenbothk.readthedocs.io/en/latest/\_images/40\_01.png)

**2. 把micro:bit 跟kittenblock 連接**

![](https://kittenbothk.readthedocs.io/en/latest/\_images/41\_01.png)

**3. 連接後，可見左側自動加載包含Robotbit的插件分欄可供使用。**

![](https://kittenbothk.readthedocs.io/en/latest/\_images/43\_1.png)

#### Python

Robotbit也支援kittenblock的python代碼編程模式

利用積木塊搭建好程序段後，點擊”舞台代碼”切換按鈕，便可立即看到micropython代碼框

![](https://kittenbothk.readthedocs.io/en/latest/\_images/44\_1.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/45\_1.png)

### FAQ常見問題與解答

#### 電池插上去沒有，打開開關沒有反應？

檢查是否已經按了電池激活按鈕？檢查電池正負是否接反？檢查電池是否有電？

***

#### 電池激活按鈕用什麽用？

在過流，或者短路，或者打開開關插拔電池這些瞬間異常大電流情況下，電池保護芯片會啟動工作，保護電路的安全性。點擊電池激活按鈕，即可恢復正常工作模式 。

***

#### 插上usb電腦找不到Microbit

robotbit上的Micro USB插口只能用於充電，不能用於下載程序。USB插到robotbit上，電腦是不會有反應的。

***

#### 電池插反會不會燒毀robotbit？

不會，robotbit的設計考慮到一般性失誤操作而做了防反接處理。插反不會供電但亦請盡量避免!

***

#### Microbit插反會不會燒毀robotbit？

不會，另外Microbit插反只會不運作。

***

#### P0引腳控制沒有反應？是不是壞了？

PO是通過跳帽默認連接到板子的蜂鳴器上，可以直接用makecode中的music模塊進行控制蜂鳴器。如果要使用P0口，需要拔掉跳帽。

***

#### Microbit上可編程IO口不止8個剩下的都去哪裏了？

Microbit上可編程IO口接近20個，但是很多已經與板子上的點陣按鍵覆用了。考慮到覆用帶來的不方便性對，新手容易帶來誤解，Robotbit 引出了8個（跟micro:bit自身沒有覆用的IO口）已經完全足夠應對日常的DIY。如果你對IO數量有狂熱的追求，可以選擇喵家另外一款擴展板IObit。

***

#### 舵機排針可以當編程IO口使用嗎？

不能，舵機s1-s8使用專門的舵機驅動芯片拓展出來，只能用於舵機驅動。

***

#### 電機接口那邊的VM有什麽用？

平時使用直流電機是用不到VM，直流電機只需要插A+A-或者B+B-。使用4相5線步進電機的時候，剛好VM就用上了，詳細請看[Robot:bit 2.0 詳細使用手冊](https://goo.gl/9E3c6Q) 。

***

#### 板子可以放在金屬表面或者潮濕環境下使用嗎？

不行，會短路的，要註意絕緣。使用前請套上隨盒附送的底座。

[底座安裝示範](https://youtu.be/FhimDxoAsj4)

***

#### 綠色端子外部電源應該接幾V電源？插高壓電會燒壞嗎？

只能接不高於6V。高於6V都會燒毀板子，電流建議2\~3A，也就是說板子最大支持的電流是3A。

***

#### 我按照教程做得，得不到實驗結果

如果實驗得不到對應的結果，請首先檢查自己的接線和程序，一般就是有些小地方遺漏了，請再三檢查下。

#### 電路板好像燒壞了，有保養嗎？

robotbit在工廠出廠都進行過硬件程序測試，保證了功能的完好性。首先先排除下是不是程序使用問題。如果你確定燒壞了，可以聯絡供應商作評估。

如評估結果為非人為損壞或自然損耗, 銷售期1年內憑單據, 香港代理會作出更換。

#### \*\*版本佚代更新說明 \*\*

Robotbit作為一款有活力的Microbit擴展板，已經經歷過兩次的迭代更新，每次的更新都是比前面一代更加貼近用家或教學需要。Robotbit版本起於2017年11月初的V1.2，中間經歷了V1.3，2018年6月中發布V2.0（由於改動提升比較大，版本直接跳到V2.0）

V2.0版本比前面版本更新的內容：

**1. 增加IO接口**

V1.3只引出3個可編程IO。 V2.0在原P0-P2基礎上增加P8、P12-P15，一共8個可編程IO足以應對平常的DIY項目。（巡線+避障so easy！）

**2. 改進電池放電方案**

充電不易發燙，但依然保持快速大電流充電的特性。

**3. 改進電源開關電路設計**

船型開關完全控制電路中所有電源的通斷，解決關閉電源待機情況下會有耗電的問題。

**4. 增加外接電源接口**

5V防反接，再外部電源的供電下，支持接大直流電機（如金屬減速電機）和大舵機（如MG995）時使用。支持的電流決定於外部電源5V的電流，Kittenbot在5V3A的外部電源支持下嘗試過驅動4個MG995沒問題。

**5. 外接電源**

VM接口的電流上限3A。

**6. 增加獨立的電池保護芯片**

摒棄前面版本的一體方案，采取高成本的獨立芯片方案，更好的應對過放過充的情況。

**7. 增加電池保護激活按鈕**

在過流、短路，或者打開開關插拔電池這些瞬間異常大電流情況下，電池保護芯片會啟動工作，保護電路的安全性。在確保更正錯誤後，點擊電池激活按鈕，即可恢復正常工作模式。

**8. 蜂鳴器改進**

上移至板頂部,增加蜂鳴器音量，讓做音樂實驗效果更加好。

**9. 采用全新40Pin立式Microbit插槽**

拔插更方便，不傷Microbit金手指。

**10. 增加5V和GND各一列排針**

為了更好兼容市面上的模塊，特意增5V和GND各一列。註意Microbit的電壓是3.3V，所以當你使用5V模塊時，Microbit只能作為輸出，不能作為輸入，否則IO口會承受5V的電壓，導致IO口損壞。新手應該在Kittenbot官方的指導下謹慎使用。

**11. 電源指示燈與充電指示燈改善**
