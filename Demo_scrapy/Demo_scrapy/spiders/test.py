import bs4
import scrapy
from ..items import DemoScrapyItem


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['lz13.cn']
    start_urls = [f'https://www.lz13.cn/lizhi/mingrenmingyan-{i}.html' for i in range(1, 200)]

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        urls = soup.select('#node-8890 > div > span:nth-child(2) > h3 > a')
        for url in urls:
            yield scrapy.Request(url=url['href'], callback=self.parse_content)

    def parse_content(self, response):
        item = DemoScrapyItem()
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        contents = soup.select('#node-8890 > div.PostContent > p')
        item['title'] = contents[0].text.strip()
        content = ''
        for tmp in contents[1:]:
            content += tmp.text
        item['content'] = content
        yield item
