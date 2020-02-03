# 知乎动态更新提醒

## 项目背景

寒假在家无聊偶然**人肉**到了****的**知乎ID**，但她更新的不怎么频繁，正好有时间，于是写了一个爬虫去检测她的知乎动态更新，一旦有动态更新，就发送到我的QQ邮箱中。

## 项目实现

本来打算通过**requests+beautifulsoup**实现，但是知乎用到了十分先进的**反爬策略**，添加**headers**仍然无法正常打开网页，于是改用**selenium**，通过**模拟登录**进行爬取。

具体使用**selenium+chrome driver**实现模拟登录，然后定位到最新的动态，每隔**4h**刷新一次，若动态更新，则发送邮件到QQ邮箱中。

## 使用方法

该项目需要安装以下库

**selenium**

**smtplib**

**email**

需要使用**chrome浏览器**以及**chrome driver** 

使用该项目需要根据自身需要修改的代码有：

**sendMail函数** 中的：

**mail_host**

**mail_user**

**mail_pass**  该密码为第三方邮件SMTP中的授权码

**sender**
**receivers**

**__main__**中的：

**uid**  该id为用户知乎网址最后的id

