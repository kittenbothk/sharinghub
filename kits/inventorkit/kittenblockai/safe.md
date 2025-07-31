# 人面辨識保險箱

![](../../../.gitbook/assets/防盗门.png)

透過人面識別技術，系統只會讓經認證過的人打開保險箱。

### 組裝說明書下載

[組裝說明書下載](https://drive.google.com/drive/folders/1wg_edUZFrqyUONA0FJ6vFBkGArRsfnf4?usp=sharing)

![](https://kittenbothk.readthedocs.io/en/latest/_images/safe_wire.png)

### 參考程式

{% file src="../../../.gitbook/assets/人面辨識保險箱 (1) (1).sb3" %}

<figure><img src="../../../.gitbook/assets/人面辨識保險箱.png" alt=""><figcaption></figcaption></figure>

### 應用玩法

{% hint style="info" %}
這應用需要使用Token。
{% endhint %}

1. 首先建立人面資料庫
2. 輸入人面名稱和建立一個獨特的組別名稱
3.  將人面放在鏡頭前，按空白鍵，程式就會進行人面辨識，將所辨識到的人面特徵儲存到資料庫

    <figure><img src="../../../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>
4.  將人面資料庫名稱填入程式

    <figure><img src="../../../.gitbook/assets/image (131).png" alt=""><figcaption></figcaption></figure>
5. 連接好Micro:bit和打開Robotbit電源
6. 點擊綠色旗啟動程式
7. 當超聲波感應器感應到5cm距離內有物件，系統就會進行人面辨識
8. 假如辨識到的人面已經在資料庫裡面，系統就會打開夾萬門
9. 按下Sugar按鍵關上鎖
10. 假如辨識到的人面不在資料庫裡面，系統就會發出警報

