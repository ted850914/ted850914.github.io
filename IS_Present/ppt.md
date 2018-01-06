## 資安期末報告-第五組
<br />
組員：廖祐德、吳珮均、曾永權、周郁祥

-----
### Lightweight Authentication Protocol for Internet of Things
### 輕量級IOT協定

----

### 何謂輕量級協定
<div class="fragment">
	<p>所謂輕量級，是指通信協議與語言、平台無關。</p>
</div>

----

### 物聯網系統中重要的協議
<div class="fragment">
	<p>MQTT &nbsp;&nbsp; COAP&nbsp;&nbsp;AMQP&nbsp;&nbsp; Rest&nbsp;&nbsp; XMPP&nbsp;&nbsp; Stomp</p>
</div>

<div class="fragment">
	<p>除了XMPP 其他皆是輕量級的協定</p>
</div>

-----

### 什麼是MQTT?
<div class="fragment">
	<p>全名為　Message Queuing Telemetry Transport</p>
</div>

<div class="fragment">
	<p>為了物聯網而設計的protocol</p>
</div>

<div class="fragment">
	<p>透過publish/subscribe的方式來做訊息傳送</p>
</div>

<div class="fragment">
	<p>類似twitter的發布訂閱機制</p>
</div>

----

### MQTT的組成元件

<div class="fragment">
	<p>分別為Publisher、Subscriber以及Topic</p>
</div>

<div class="fragment">
	<p> Publisher為訊息的來源，它會將訊息發送給Topic<br>
	Subscriber向Topic註冊，表示想接收此Topic訊息</p>
</div>

<div class="fragment">
	<img src="https://goo.gl/Ja2yd7">
</div>

----

### MQTT的特性
<div class="fragment">
	<p>提供一對多的訊息分配</p>
</div>

<div class="fragment">
	<p>使用TCP/IP提供網路連接</p>
</div>

<div class="fragment">
	<p>header固定長度為2byte，可減少封包傳送負載</p>
</div>

----

### 三種訊息傳送方式

<div class="fragment">
	<p>At most once <br>
       最多一次，訊息可能會遺失
	</p>
</div>

<div class="fragment">
	<p>At least once<br>
	   至少一次，保證訊息送達，只是可能重複傳送</p>
</div>

<div class="fragment">
	<p>Exactly once<br>
	   確定一次，重複收到資料或資料遺失會造成系統錯誤</p>
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
	<p>知名應用:Facebook Message App</p>
</div>

-----

### 什麼是CoAP?

<div class="fragment">
	<p>全名為 The Constrained Application Protocol</p>
</div>

<div class="fragment">
	<p>已是IETF標準</p>
</div>

<div class="fragment">
	<p>屬於輕量版的HTTP/UDP，有利於感測節點進行網路傳輸</p>
</div>

----
### COAP的特點

<div class="fragment">
	<p>Client/Server架構</p>
</div>

<div class="fragment">
	<p>多半為CoAP Server提供資源，由CoAP Client請求讀取/控制資源狀態</p>
</div>

<div class="fragment">
	<p>使用UDP，是否重新傳送由應用層決定</p>
</div>

----

### COAP的封包

<div class="fragment">
	<p>採用二進位整數格式</p>
</div>

<div class="fragment">
	<p>封包標頭4個byte而非HTTP使用字串格式</p>
</div>

<div class="fragment">
	<p>傳送時負擔小，且不必耗時解析字串</p>
</div>

----

### COAP QOS

<div class="fragment">
	<p>訊息分為Confirmable或Non-Confirmable</p>
</div>

<div class="fragment">
	<p>前者要求接收端傳回ack，若沒收到則重送一次</p>
</div>

<div class="fragment">
	<p>後者不在乎接收端是否有收到</p>
</div>

-----

### CoAP  &nbsp; vs &nbsp; MQTT &nbsp; 比較

<div class="fragment">
	<p>都是公開標準且都是基於IP層的協定</p>
</div>

<div class="fragment">
	<p>封包標頭小且採用binary格式</p>
</div>

<div class="fragment">
	<p>CoAP屬於一對一通訊，MQTT則是多對多 </p>
</div>

