# scrapy demo
## 修改国内源
pip install -i http://mirrors.aliyun.com/pypi/simple/ scrapy (临时)
### 永久修改方法
cmd %APPDATA%
新建pip目录->pip.ini
```
[global]
index-url=http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
```
## 升级pip 
>pip show pip
>python -m pip install --upgrade pip
>python -m pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple/
## 安装 scrapy
>pip install scrapy
## 创建项目
>scrapy startproject scrapy_demo 

spiders: 文件夹用于存放爬虫程序 \
items: 用于存放一些存储对象，比如本例中的图片的url \
middlewares: 是用来定义中间件 \
pipelines: 是用于把我们需要存储的item对象进行存储，也就是根据pic_url来下载图片存储在本地 \
settings: 是用于对scrapy工作的一些属性进行设置 

## [参考](http://www.manongjc.com/detail/16-rdlxozmigggocep.html)