import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DemoScrapyItem
import bs4


class Test2Spider(CrawlSpider):
    name = 'test2'
    allowed_domains = ['lz13.cn']
    start_urls = ['https://www.lz13.cn/lizhi/mingrenmingyan-1.html']

    rules = (
        # 详情页URL
        Rule(LinkExtractor(allow=r'www.lz13.cn/mingrenmingyan/\d+.html'), callback='parse_item'),
        # 翻页 follow深度爬取 restrict_xpaths限制规则
        Rule(LinkExtractor(allow=r'www.lz13.cn/lizhi/mingrenmingyan-\d+.html',
                           restrict_xpaths='//div[@class="pager"]/a'), follow=True),
    )

    def parse_item(self, response):
        item = DemoScrapyItem()
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        contents = soup.select('#node-8890 > div.PostContent > p')
        item['title'] = contents[0].text.strip()
        content = ''
        for tmp in contents[1:]:
            content += tmp.text
        item['content'] = content
        yield item
