# 閉合電路實驗模組

<figure><img src="../.gitbook/assets/conductivity1.png" alt=""><figcaption></figcaption></figure>

這是一個可以測量物料導電性的模組,可以測量到電流讀數.

## 產品參數

* 接口: I2C
* 類型: I2C 模組

## 產品接線

### FutureLite AI

<figure><img src="../.gitbook/assets/conductivity_futurelite_wiring.png" alt=""><figcaption></figcaption></figure>

## 使用教學

#### 1. 打開模組上蓋,放入2粒AAA電池

<figure><img src="../.gitbook/assets/conductivity3.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/conductivity6.png" alt=""><figcaption></figcaption></figure>



#### 2. 蓋上上蓋,連接鱷魚夾線

<div><figure><img src="../.gitbook/assets/conductivity2.png" alt=""><figcaption></figcaption></figure> <figure><img src="../.gitbook/assets/conductivity4.png" alt=""><figcaption></figcaption></figure></div>

#### 3. 接上要測試的物料,然後打開開關

<figure><img src="../.gitbook/assets/conductivity5.png" alt=""><figcaption></figcaption></figure>

#### 4. 假如物料能夠導電，模組上的紅色LED會亮起

<figure><img src="../.gitbook/assets/conductivity7.png" alt=""><figcaption></figcaption></figure>

## 產品示範

### 在連接不同導電性的物料時，量度到的電流會變化，導電性能越高電流就越高。

### 1. 連接220ohm電阻: 1.12mA

<figure><img src="../.gitbook/assets/conductivity8.png" alt=""><figcaption></figcaption></figure>

### 2. 連接鍍錫銅線: 1.32mA

<figure><img src="../.gitbook/assets/conductivity10.png" alt=""><figcaption></figcaption></figure>

### 3. 連接螺絲: 1.34mA

<figure><img src="../.gitbook/assets/conductivity11.png" alt=""><figcaption></figcaption></figure>

### 4. 沒有連接任何物料: 0mA

<figure><img src="../.gitbook/assets/conductivity9.png" alt=""><figcaption></figcaption></figure>

## 編程教學

### MakeCode 編程教學

#### 在擴展頁輸入以下插件網址

#### 感應器Plus插件：[https://github.com/kittenbothk/pxt-ModulePlus](https://github.com/kittenbothk/pxt-ModulePlus)

<figure><img src="../.gitbook/assets/image (287).png" alt=""><figcaption></figcaption></figure>

#### 詳細方法

#### 閉合電路實驗模組積木塊：

<figure><img src="../.gitbook/assets/image (288).png" alt=""><figcaption></figcaption></figure>

#### 閉合電路實驗模組編程

{% embed url="https://makecode.microbit.org/_ivpJ2dUdiDMw" %}

[參考程式網址](https://makecode.microbit.org/_ivpJ2dUdiDMw)

#### 插件版本與更新

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](https://kittenbothk.readthedocs.io/en/latest/Makecode/makecode_extensionUpdate.html)
