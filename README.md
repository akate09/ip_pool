# ip_pool
主要是参考了网上作者小四毛的框架，github网址可以参考：https://github.com/xiaosimao/IP_POOL

不过他的框架跑起来问题很多，实际可以获取的ip很少。因此
我对此框架进行了相关bug的处理，终于能够运行起来了~~
说明如下：
首先data5u这个网站是要带header和cookie去访问的，不然分分钟403，因此在proxie_basic_config.py做出了修改
其次在他写的另外一个爬虫框架中（请参考我上传的aispider库）的page_downloader.py中，对return的内容进行了修改，不然会出现None object is not callable错误

其他还有一些细微的改动。。想直接运行的朋友可以直接下载我的代码，运行过程可以参考小四毛的github，他的说明很详细。
