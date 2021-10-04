import scrapy
from scrapy_demo.items import ScrapyDemoItem
# 值得注意的是spider中的函数均为生成器函数，不是用return，而是用yield关键字返回数据，
# 其原因简单说来就是这些方法在引擎调用时是作为回调函数（twisted.inlineCallback）绑定到请求的回调链中，
# 在处理完一个response之后需要用yield挂起等待下一个调用。所以这些方法不能以普通函数的形式调用，
# 直接调用返回的只是一个生成器对象，另外，由于异步并发的原因，方法内部也非一次就能执行一遍，
# 在yield挂起之后将在下一个事件循环中才继续往下执行
class MySpider(scrapy.Spider):
    # spider类中有类属性“name”，scrapy就是根据这个类属性来区分同一工程项目下不同的爬虫
    name = ''
    allowed_domains = ['']
    
    # 一次爬取开始于一个或若干起始URL，一般会默认存放于类属性start_urls中，
    # 默认由start_request方法遍历其中的URL并以GET方法请求，
    # 该方法默认将发出的请求会绑定parse方法作为回调函数（callback）
    def start_requests(self):
        yield scrapy.Request('', self.parse)
    
    # request对象的callback属性的值为spider类中的一个方法（非执行结果），
    # 引擎将request交给下载器处理之后等待下载器获得响应，当下载器返回响应信息，
    # 引擎将调用上述request的callback属性指明的函数处理响应
    
    # Spider类中的方法最主要功能就是作为请求的回调函数来处理请求的响应信息。
    # 接收一个参数：response对象，该对象中包含了响应的所有信息包括响应状态码（status）、
    # 响应头（headers）、响应体（body）和响应文本（text）等。
    # 另外，response对象还封装了解析html的选择器工具Xpath（css选择器路径将首先被转换为xpath路径）
    def parse(self, response):
        
        for h3 in response.xpath('//h3').getall():
            yield ScrapyDemoItem(title=h3)
            
        for href in response.xpath('//a/@href').getall():
            yield scrapy.Request(response.urljoin(href), self.parse)
            