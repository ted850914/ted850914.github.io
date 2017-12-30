## 什麼是 git ?
 "分散式"版本控制系統

 後續補充
----

## 為什麼要學 git ?
ex:[大一專題](https://www.facebook.com/groups/1597697557217011/files/)
<div class="fragment">
 <p>git 類似遊戲打王的S/L大法</p>
</div>


-----


## git 的優缺點 ##
### 優點
<div class="fragment">
 	<p>1.免費、開源 </p>
</div>

<div class="fragment">
	 <p>2.速度快</p>
</div>

<div class="fragment">
	 <p>3.檔案小(只記錄版本間的差異)</p>
</div>
 
<div class="fragment">
	 <p>4.分散式系統</p>
</div>

----


## git 的優缺點 ##
### 缺點
<div class="fragment">
 	<p>1.易學難精 </p>
</div>

<div class="fragment">
 	<p>2.指令式介面比GUI好用，但容易讓人卻步</p>
</div>

<div class="fragment">
 	<p>3.沒有動畫</p>
</div>

-----

## git  v.s  github
### 差異
???

-----


## 如何安裝 git

<div class="fragment">
	<a href="https://git-scm.com/download/win">安裝網址</a>
</div>

<div class="fragment">
	<p>安裝過程都直接next</p>
</div>

----

## 驗證是否成功安裝
找到git bash後開啟
```
$git --version
git version 2.14.1.windows.1
```
出現類似訊息代表成功

-----

## 指令介紹

----

## 切換目錄 

切換到指定目錄 cd ./~
```
$cd desktop/test
```

----

## 初始化

初始化目錄，使git開始版本控制
```
$git init
```

----

## 移除控制

刪除 .git　資料夾

任何東西都救得回來，但.git被刪了就沒辦法

----

## 狀態

顯示未被追蹤、被追蹤的檔案名稱

```
$git status 
```

----

## 加入暫存區

把指定的檔案加入暫存

--all:把所有改變的檔案加入暫存

git add(*html, --all,...)

```
$git add ptt.html
$git add --all
```

----

## 把暫存區裡的檔案存檔

將暫存區的檔案永久存檔

git commit -m ""

""內輸入文字說明這次改變了甚麼東西

說明要具體，例如修bug，不要輸入"bug fixed"

"line 38~52 bug fixed"這樣比較好

``` 
$git commit -m "line 38~52 bug fixed"
```

----

## git 的三個區塊

<a href="https://gitbook.tw/images/using-git/working-staging-and-repository/all-states.png">圖片</a>

----

## 何時要 commit?

1. 完成了一個任務
1. 工作告一段落(下班、休息)
1. 你想要的時候

----

## 顯示紀錄

1. 是誰 commit（人是誰殺的）
1. 什麼時候 commit （什麼時候殺的）
1. commit 時做了什麼事 （怎麼殺的）

git log (--oneline,--graph)

```
$git log --oneline
```

----

## 移除檔案

git rm (--cached,*.txt)

--cached:只是讓git不再控管這個檔案，並非刪除

*.txt:刪除所有txt檔案

```
$git rm --cached hello.txt
```

----

## 改檔名

git mv
```
$git mv hello.txt world.txt
```

----

## 改commit訊息

```
$git commit --amend -m "restore commit msg"
```

----

## 回復到先前版本

git reset e12d8ef^:回復到e12d8ef的前一版本

git reset e12d8ef~3:回復到e12d8ef的前三版本

e12d8ef:每個版本的編號，可用 git log --oneline查看

```
$git reset e12d8ef~3
```
