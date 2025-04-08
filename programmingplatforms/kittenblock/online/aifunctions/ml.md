# Kittenbot機器學習

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

圖像辨識，姿態分類和音頻分類

## 模型訓練教學

首先打開模型訓練工具。

<figure><img src="../../../../.gitbook/assets/image (96).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (97).png" alt=""><figcaption></figcaption></figure>

## 圖像辨識

在圖像辨識工具裡面，您可以使用電腦鏡頭或者上傳圖片作訓練。

在這個教學我們會試試用電腦鏡頭訓練包剪揼模型。

<figure><img src="../../../../.gitbook/assets/image (98).png" alt=""><figcaption></figcaption></figure>

將分類名稱改為Rock，然後在鏡頭面前做出揼的手勢。

<figure><img src="../../../../.gitbook/assets/image (99).png" alt=""><figcaption></figcaption></figure>

按著錄製按鍵，就可以將鏡頭畫面加入樣本庫。

<figure><img src="../../../../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

重複同樣步驟，添加包的圖片樣本。

<figure><img src="../../../../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

最後可以添加類別，完成剪的樣本錄製。

<figure><img src="../../../../.gitbook/assets/image (103).png" alt=""><figcaption></figcaption></figure>

完成後按下訓練模型，平台就會自動生成圖像辨識模型。

<figure><img src="../../../../.gitbook/assets/image (104).png" alt=""><figcaption></figcaption></figure>

訓練完成後平台會提供即時的預覽，假如效果未如理想可以繼續錄入樣本重新訓練。否則就可以按使用模型，將模型導入程式中。

<figure><img src="../../../../.gitbook/assets/image (105).png" alt=""><figcaption></figcaption></figure>

導入後，相應的編程積木就會自動生成出來。

<figure><img src="../../../../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
儲存程式時不會儲存模型，如需保留模型請記住要儲存模型供下次使用。
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

### 參考程式

<figure><img src="../../../../.gitbook/assets/image (108).png" alt=""><figcaption></figcaption></figure>

{% file src="../../../../.gitbook/assets/kittenblock_ml1.sb3" %}

參考模型

{% file src="../../../../.gitbook/assets/teachable-machine_image.zip" %}

## 姿態分類

姿態分類是訓練模型辨識人體的姿態，訓練過程和圖像辨識相似。

<figure><img src="../../../../.gitbook/assets/image (109).png" alt=""><figcaption></figcaption></figure>

鏡頭會自動追蹤人體的頭部與四肢，因此模型訓練後即使是不同人測試，模型也能準確辨認姿勢。

<figure><img src="../../../../.gitbook/assets/image (110).png" alt=""><figcaption></figcaption></figure>

### 參考程式

<figure><img src="../../../../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

{% file src="../../../../.gitbook/assets/kittenblock_ml2.sb3" %}

參考模型

{% file src="../../../../.gitbook/assets/teachable-machine_pose.zip" %}



## 音頻分類

音頻分類可以訓練模型辨認不同的音頻。

<figure><img src="../../../../.gitbook/assets/image (112).png" alt=""><figcaption></figcaption></figure>

首先需要錄入背景噪音作為基準，錄入完成後按提取樣本。

<figure><img src="../../../../.gitbook/assets/image (114).png" alt=""><figcaption></figcaption></figure>

錄製音頻並提取樣本。

<figure><img src="../../../../.gitbook/assets/image (115).png" alt=""><figcaption></figcaption></figure>

完成後訓練模型，平台亦會即時顯示分類結果。

<figure><img src="../../../../.gitbook/assets/image (116).png" alt=""><figcaption></figcaption></figure>

### 參考程式

<figure><img src="../../../../.gitbook/assets/image (117).png" alt=""><figcaption></figcaption></figure>

{% file src="../../../../.gitbook/assets/kittenblock_ml3.sb3" %}

參考模型

{% file src="../../../../.gitbook/assets/teachable-machine_audio.zip" %}

## 模型載入

如要載入先前儲存的模型，只需打開模型訓練工具然後按墮入訓練項目即可。

<figure><img src="../../../../.gitbook/assets/image (118).png" alt=""><figcaption></figcaption></figure>
