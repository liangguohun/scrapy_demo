# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class ScrapyDemoSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

# 中间件的设置与开启在Settings模块中，以字典的形式表现，
# key为中间件模块的导入路径（同import路径），value为一个整数，
# 表示该中间件的权重。对于下载中间件来说，权重越小，离引擎就越近，
# 权重越大越靠近下载器。在处理Request和Response的时候都是按经过顺序依次进行

# 中间件就是一个钩子，可以拦截并加工甚至替换请求和响应，
# 可以按照我们的意愿来控制下载器接受和返回的对象。
# 而由于爬虫工作的过程主要是处理各种请求和响应，所以下载中间件可以极大地控制爬虫的运行
class ScrapyDemoDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
# 在请求经过时被调用，它接受两个参数：request和spider，在引擎调用的时候会默认传入，
# 分别为待处理的request对象和产生该请求的spider对象，在这个方法中可以对request对象进行加工，
# 增加其属性或在META字典中增加字段来传递信息。这个方法允许返回request对象或返回一个
# IgnoreRequest异常或者无返回（即返回None）。在返回request对象时，这个对象不会再传递给接下来的中间件，
# 而是重新进入调度器队列中等待引擎调度。返回异常时该异常会作为中间件process_exception方法的参数传入，
# 若无process_exception方法，则会交给该请求err_back绑定的方法处理。若无返回则将request对象交给下一中间件处理
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None
# 在响应被返回经过时调用，接受3个参数，分别为request对象，response对象和spider对象。
# spider对象同上，response对象为下载器返回的响应，而request对象则表示产生该响应的请求，
# 与spider中的response有所不同，此处的response对象中没有request属性，而是同作为参数传入。
# 在这个方法中可以对下载器返回的响应进行处理，包括响应的过滤，校验，
# 以及与process_request中耦合的操作，如Cookie池和代理池的操作等。
# 该方法允许3中返回：request对象，response对象和IgnoreRequest异常。
# 当返回request对象时同上一方法，当返回response对象时，该response会交由下一中间价继续处理，
# 而返回异常则直接交给该请求err_back绑定的方法处理
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response
# 在下载器或prcoess_request返回异常时被调用，接受3个参数：request对象，exception对象和spider对象，
# 其中request对象为产生该异常的请求。它有3种返回分别为request对象，response对象和无返回。
# 当无返回时，该异常将被后续的中间件处理；当返回request对象和response对象时，
# 均不会再调用后续的process_exception方法，前者将会交给调度器加入队列，后者将会交由process_response处理
    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
