from scrapy import Spider,Request
from tencent.items import TencentItem
from lxml import etree





class TencentspiderSpider(Spider):
    name = 'tencentspider' #爬虫名
    allowed_domains = ['tencent.com'] #指定爬取的域名





    def start_requests(self):
        for i in range(0,500,10):
            url = 'https://hr.tencent.com/position.php?&start={}'.format(str(i))
            yield Request(url = url,callback=self.parse)


    def parse(self, response):
        #获取所有tr列表标签
        selector = etree.HTML(response.text)
        node_list = selector.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        #node_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')

        for node in node_list:
            item = TencentItem()
            item['positionName'] = node.xpath('./td[1]/a/text()')


            item['positionLink']=node.xpath('./td[1]/a/@href')

            if len(node.xpath('./td[2]/text()')):
                item['positionType'] = node.xpath('./td[2]/text()')
            else:
                item['positionType'] = ""


            item['peopleNumber']=node.xpath('./td[3]/text()')
            item['workLocation']=node.xpath('./td[4]/text()')
            item['publishTime']=node.xpath('./td[5]/text()')
            yield item






