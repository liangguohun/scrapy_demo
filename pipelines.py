# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import urllib3
import os
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 数据管道是Scrapy中处理数据的组件。当spider中的方法yield一个字典或scrapy.Item类及其子类时，
# 引擎会将其交给pipelines处理。Pipelines和中间件十分类似，数据条目将以此通过pipeline进行处理，
# pipeline的权重越小，则越早被调用
class ScrapyDemoPipeline:
    def __init__(self):
        self.cnt = 1
        dir_path = './pic'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            
    def process_item(self, item, spider):
        for pic_url in item['pic_urls']:
            print(pic_url)
            pic_name = str(self.cnt)+'.jpg'
            pic = urllib3.urlopen(pic_url).read()
            file = open('./pic/'+pic_name, 'wb')
            file.wirte(pic)
            file.close()
        return item
