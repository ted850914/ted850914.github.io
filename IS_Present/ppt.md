## 資安期末報告-第五組
<br />
組員：廖祐德、吳珮均、曾永權、周郁祥

-----
### 題目一
<p>Lightweight Authentication Protocol for Internet of Things</p>
### IOT輕量級協定

----

### 什麼是輕量級協定？
<div class="fragment">
	<p>假設今天一個節點要認證需要花1毫秒</p>
</div>
<div class="fragment">
	<p>那一千個節點就需要1秒</p>
</div>
<div class="fragment">
	<p>那一千萬個節點就需要1000秒</p>
</div>
<div class="fragment">
	<p>所以要縮短驗證的時間->將協定輕量化</p>
</div>

----

### 物聯網系統中重要的輕量級協定
<div class="fragment">
	<p>MQTT &nbsp;&nbsp; COAP&nbsp;&nbsp; AMQP&nbsp;&nbsp; Stomp</p>
</div>
<div class="fragment">
	<p>還有非常非常多，在這裡只介紹MQTT和CoAP</p>
</div>

-----

### MQTT
<div class="fragment">
	<p>全名為 Message Queuing Telemetry Transport</p>
</div>

<div class="fragment">
	<p>透過publish/subscribe的方式來做訊息傳送</p>
</div>

<div class="fragment">
	<p>類似Twitter、Youtube的發布訂閱機制</p>
</div>

----

### MQTT的組成元件

<div class="fragment">
	<p>分別為Publisher、Subscriber以及Topic</p>
</div>

<div class="fragment">
	<p>Publisher為訊息的來源，它會將訊息發送給Topic</p>
	<p>Subscriber向Topic註冊，表示想接收此Topic訊息</p>
	<img src="https://goo.gl/Ja2yd7">
</div>

----

### MQTT的特性

<div class="fragment">
	<p>header固定長度為2 bytes，使用Binary格式</p>
</div>

<div class="fragment">
	<p>底層走TCP</p>
</div>

<div class="fragment">
	<p>提供一對多的訊息分配</p>
</div>

<div class="fragment">
	<p>可以留下"最後遺囑"，通知訂閱者用戶端與 MQTT 伺服器的連線異常中斷</p>
</div>

----

### MQTT 協定格式
<img src="http://designer.mech.yzu.edu.tw/articlesystem/article/compressedfile/(2016-07-15)%20%E7%AC%AC%E4%B8%89%E7%AB%A0%20MQTT%E9%80%9A%E8%A8%8A%E5%8D%94%E8%AD%B0.files/image003.png">
<p class="fragment">Fix Header：固定的2 byte</p>
<p class="fragment">Variable Header：參數設置</p>
<p class="fragment">Payload：訊息主要的內容，可以帶入字串訊息、圖片、影片等類型檔案</p>

----

### 三種訊息傳送方式

<div class="fragment">
	<p>最多一次，但訊息可能會遺失</p>
</div>

<div class="fragment">
	<p>至少一次，保證訊息送達，只是可能重複傳送</p>
</div>

<div class="fragment">
	 <p>確定一次，重複收到資料或資料遺失會造成系統錯誤</p>
</div>

----

### MQTT的現況

<div class="fragment">
	<p>並非一個標準化的protocol，還在改進</p>
</div>

<div class="fragment">
	<p>IBM對此協定採開放、免授權費的方式讓大家使用</p>
</div>

<div class="fragment">
	<p>支援C、Java、Javascript、C++等等的語言</p>
</div>

<div class="fragment">
	<p>低頻寬、低硬體需求的特性，使得MQTT十分適合在手機上做應用</p>
</div>

<div class="fragment">
	<p>知名應用：Facebook messenger App</p>
</div>

-----

### CoAP

<div class="fragment">
	<p>全名為 Constrained Application Protocol</p>
</div>

<div class="fragment">
	<p>使用 client/server 架構</p>
</div>

----

### COAP的特點

<div class="fragment">
	<p>封包標頭4個byte，使用Binary格式</p>
</div>

<div class="fragment">
	<p>底層走UDP</p>
</div>

<div class="fragment">
	<p>支援觀察模式</p>
</div>

----

### COAP 協定格式

<p class="fragment" style="font-size:35px">Version：版本號碼。</p>
<p class="fragment" style="font-size:35px">Message Type：CON，NON，ACK，RST。</p>
<p class="fragment" style="font-size:35px">Message ID：每個CoAP訊息都有一個ID，在一次Session中ID總是保持不變。但在這個Session之後該ID會被回收利用。</p>
<p class="fragment" style="font-size:35px">Options：包括CoAP Port，CoAP主機和CoAP查詢字符串等。</p>
<p class="fragment" style="font-size:35px">Payload：要傳遞的資訊。</p>

----

### Message Type

<div class="fragment">
	<p>CON：Confirmable或Non-Confirmable</p>
	<p>要求接收端傳回ACK，若沒收到則重送一次</p>
</div>
<br />
<div class="fragment">
	<p>NON：Non-Confirmable</p>
	<p>不在乎接收端是否收到</p>
</div>

-----

### MQTT  &nbsp; vs &nbsp; CoAP

<div class="fragment">
	<p>MQTT是走TCP，CoAP是走UDP</p>
</div>

<div class="fragment">
	<p>MQTT是多對多，CoAP是一對一通訊</p>
</div>

<div class="fragment">
	<p>MQTT封包Header為2Byte，CoAP封包Header為4Byte</p>
</div>

-----

### 題目二
<p>Perform public-key distribution scenario described</p>

----

<img src="img/KDC.jpg">

----

## DEMO

-----

### 分工

<p>廖祐德：PPT二版、題目二程式碼</p>
<p>曾永權：PPT初版</p>
<p>吳珮均：資料蒐集</p>
<p>周郁祥：Word</p>

----

### 參考資料

<p>http://3smarket-info.blogspot.tw/2017/05/iot-mqtt-coap.html</p>
<p>https://www.ithome.com.tw/voice/92179</p>
<p>https://kknews.cc/zh-tw/tech/kam6aev.html</p>
<p>https://goo.gl/vN9hdh</p>
