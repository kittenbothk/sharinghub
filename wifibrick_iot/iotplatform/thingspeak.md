# ThingSpeak

說到IoT (物聯網)教學, 不能不提[thingspeak](https://thingspeak.com/)

它是一個由Mathworks管理, 強大的IoT 分析服務端平台, 讓用家可以把設備(如sensor)所收集的數據, 經過網絡傳送到該平台上 (REST API / MQTT 協議) , 以圖像型式把數據程現或作雲端數據分析。當然, 我們也可以通過thingspeak進行數據互換, 把由A 點上傳的數據, 推送到B點設備上作進一步判斷或應用, 進行實時數據交換。

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/iot-01-01.png" alt=""><figcaption></figcaption></figure>

thingspeak是其中一個現時最多新手選用的IoT 平台, 有免費版本也有商用版; 對於剛接觸的初學用家而言, 免費版本的thingspeak 是個不錯的選擇。

更多關於Licence[說明](https://thingspeak.com/pages/license_faq)

### 登記帳戶

正式使用thingspeak 前, 我們需先登記一個帳戶; 如上文提及, 一般新用戶可先登記一個免費帳戶進入平台

![](https://kittenbothk.readthedocs.io/en/latest/_images/iot-02-01.png)

新用戶選Create Acconut; 已登記過的就直接Sign In 便可

![](https://kittenbothk.readthedocs.io/en/latest/_images/iot-03-01.png)

填好資料後便按下Continue

![](https://kittenbothk.readthedocs.io/en/latest/_images/iot-04-01.png)

在選項上打剔便可繼續登記程序。

![](https://kittenbothk.readthedocs.io/en/latest/_images/iot-05-01.png)

跟據指示, 到所用的郵箱找回確認電郵並完成第2點的核實程序。**此頁面需保留**

![](https://kittenbothk.readthedocs.io/en/latest/_images/iot-06-01.png)

在郵件中點選連結, 完成確認程序。

![](https://kittenbothk.readthedocs.io/en/latest/_images/iot-07-01.png)

![](https://kittenbothk.readthedocs.io/en/latest/_images/iot-08.png)

然後我們需要返回上一頁面, 點選第3項的continue

![](https://kittenbothk.readthedocs.io/en/latest/_images/iot-09-01.png)

為帳號設定password

![](https://kittenbothk.readthedocs.io/en/latest/_images/iot-10-01.png)

帳號登記成功

![](https://kittenbothk.readthedocs.io/en/latest/_images/iot-11-01.png)

### ThingSpeak平台設置

申請帳號之後，我們還未可以開始編程，因為我們要先在ThingSpeak設置好平台。

#### 建立新頻道

在My Channel的頁面建立新頻道。

![](../../.gitbook/assets/1.png)

除了頻道名稱之外其他可以不用理會。

![](<../../.gitbook/assets/2 (1).png>)

完成之後就可以按Save Channel。

![](<../../.gitbook/assets/3 (1).png>)

進入Sharing。

![](../../.gitbook/assets/4.png)

最方便和簡單地使用ThingSpeak的方法是將頻道設為公開，所以我們選擇第二個選項。

![](../../.gitbook/assets/5.png)

當你看到Access由Private變為Public就代表頻道完成了。

![](<../../.gitbook/assets/6 (1).png>)

#### 添加新裝置

然後請前往Devices，選擇MQTT。

![](../../.gitbook/assets/8.png)

添加一個新裝置。

![](../../.gitbook/assets/9.png)

選擇剛才建立的頻道，點擊Add Channel。

<div><img src="../../.gitbook/assets/10.png" alt=""> <figure><img src="../../.gitbook/assets/11.png" alt=""><figcaption></figcaption></figure></div>

最後就可以點擊Add Device。

添加裝置後，這一個頁面非常重要！這些是大家的未來板用來連接ThingSpeak的登入資料，請大家自行記下，或者下載登入資料，儲存在電腦。

![../../\_images/128.png](../../.gitbook/assets/12.png)

![](../../.gitbook/assets/13.png)
