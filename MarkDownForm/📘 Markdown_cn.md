# ✨ 1. 标题（Headers）

使用 `#` 表示标题，1 个 `#` 是一级标题，2 个是二级，依此类推。最多6个
‘ # 一级标题 
## 二级标题 
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
---

# 📄 2. 段落与换行

### 空行方式：
- 双空白+回车
- 句尾加\，当然，这个不总是有效
-  html语法< br > 当然里面不应该有空格
这是双空白  
这是斜杠\
这是html语法br<br>
&emsp;不要用空格（spaces）或制表符（ tabs）缩进段落。Markdown 本身**不支持传统意义的段落缩进**，&emsp;可以当作特殊情况使用

---

# 🔠 3. 字体样式

**双星号加粗** 
*单星号斜体* 
***三星号加粗斜体*** 
~~双波浪删除线~~ 
星号=下划线

---

# 📢4.引用语法

> 用>可以创建出一个高亮的引用卡片
> > 可以多层引用，使用多个>>
> ## 引用内也可以使用md语法
> - 像这样
> - **像这样**

---

# ✅ 5. 列表语法
## 有序列表
1. 一
2. 二
3. 三
4. 四
此外，只要这个列表满足从1.开始，后面不管你写什么"数字".那都会自动排序

## 无序列表：
- 破折号
* 星号
+ 加号
+ 都会自动变成列表
    如果想保留排序添加一些别的，可以在前面打四个空格
> 用引用符号也行

1. 嵌套列表
    - 像这样
    - 像这样
2. 像这样

---

# 💻 6. 代码语法

## 行内代码：

使用反引号 `` ` `` 包裹：
这是 `print("Hello")` 的用法。
如果代码内包含反引号，用
``双引号``
```或者使用三引号 ```

---

# 🔻 7. 分隔线语法

在一行输入多个-, * ,_即可
`--- *** ___`

---

# 🔗 8. 链接语法


`[链接文字](https://example.com)`

[markdown教程](https://markdown.com.cn/)


---

# 🖼️ 9. 图片语法


本地链接
[![小猪图片](.\pict\pig.jpg "小猪" )](https://www.google.com/search?newwindow=1&sca_esv=49266cf56d93934f&sxsrf=AE3TifMiVBoxiiBNHQKyy7kf0FoESSn8Wg:1753423127413&q=%E5%B0%8F%E7%8C%AA&udm=2&fbs=AIIjpHyUpTfRVK7rDoqlzWEDmpyV0ik-IFrYG35KMbRhURnOYjotTZXM-wzUQk0zctqhoqM3mwYKtkdMMy5ehZjlthVlVhLSXBuy3mObBFmzM6MavOxLnGy951i8TkHbgq31-fcIyhWywchyillMZKKZkJqaW0Wv9ARs-s1Ob3nP_czB6t5WyO0XIufGIPAi8r-ds963VumAFvGDluD38pIntBgixNH8-_i_vFKsEI2mVoEvo42VGc03P7w8JNOmT2EXFDhAVPNO&sa=X&ved=2ahUKEwj15pmVqteOAxVFm68BHUYLAdEQtKgLKAF6BAgfEAE&biw=998&bih=470&dpr=1.25)

网络链接
[![RUNOOB 图标](https://static.jyshare.com/images/runoob-logo.png)](https://www.runoob.com/markdown/md-image.html)


🧠 图片本质就是“带叹号的链接”。

---

# 🔤 10. 转义字符语法

为了保证安全，对于单独的星号等符号最好加上\
\* \会自动被忽视

此外，在html的语法里，`<` 和 &比较特殊，需要专门写成实体
`&lt;` 和 `&amp;`

不过markdown会自动转义保证安全
AT&T is big.
4 < 5
👉 Markdown 会自动变成：
AT&amp;T is big.
4 &lt; 5

---

# 🧱 11. 内嵌 HTML 标签

你可以嵌入任意 HTML 元素：

<b>加粗</b>  
<mark>高亮</mark> <details><summary>点击展开</summary>隐藏内容</details>

markdown支持html语法

---

# 🧾 12. Markdown 表格语法

Markdown 支持用 `|` 管道符 来创建表格，使用 `-` 来定义表头和对齐方式。
`
| Syntax      | Description | 
|-------------|-------------| 
| Header      | Title       |
| Paragraph   | Text        |`

🧠 渲染效果：

| Syntax    | Description |
| --------- | ----------- |
| Header    | Title       |
| Paragraph | Text        |

---

### 📌 表格语法说明：

- 表头与表体用 `---` 分隔
- 每列用 `|` 分隔（首尾可以有也可以没有）
- 每行要**列数一致**
- Markdown 会自动将表格格式化成 HTML 表格

---

## 📐 对齐方式设置（在分隔线中用冒号 `:` 表示）

| 左对齐 | 居中对齐 | 右对齐 |
| :-- | :--: | --: |
| 苹果  |  香蕉  |  橙子 |
| 车   |  飞机  |  火箭 |

`| 左对齐 | 居中对齐 | 右对齐 | 
|:-------|:--------:|--------:| 
| 苹果   | 香蕉     | 橙子    |
| 车     | 飞机     | 火箭    |`
