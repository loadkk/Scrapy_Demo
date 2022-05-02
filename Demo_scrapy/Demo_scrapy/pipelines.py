# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DemoScrapyPipeline:
    def process_item(self, item, spider):
        self.write.write(item['title'] + ' | ' + item['content'] + '\n')
        return item

    def open_spider(self, spider):
        self.write = open('res.txt', 'a+', encoding='utf8')

    def close_spider(self, spider):
        self.write.close()
