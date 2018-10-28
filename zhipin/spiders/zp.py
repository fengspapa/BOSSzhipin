# -*- coding: utf-8 -*-
import scrapy
from zhipin.items import ZhipinItem

class ZpSpider(scrapy.Spider):
    name = 'zp'
    #allowed_domains = ['zhipin.com/']
    start_urls = ['https://www.zhipin.com/']
   # start_urls = ['https://www.zhipin.com/c101280100-p100101/?page=1']

    def parse(self, response):
        href_list = response.xpath('//*[@class="text"]/a/text()').extract()
        for i in href_list:
            new_href = 'https://www.zhipin.com/c101280100/?query='+i+'&page=1'
            yield scrapy.Request(url = new_href,callback=self.run)

    def run(self,response):
    	li_list = response.xpath('//*[@id="main"]/div/div[2]/ul/li')
    	for i in li_list:
    		item = ZhipinItem()
    		item['name'] = i.xpath('.//div[@class="job-title"]/text()').extract_first()#职位名称
    		item['money'] = i.xpath('.//span[@class="red"]/text()').extract_first()#工资
    		item['company'] = i.xpath('.//div[@class="company-text"]/h3/a/text()').extract_first()#公司名称
    		item['city'] = i.xpath('.//div[@class="info-primary"]/p/text()').extract()[0]#工作地址
    		item['work_year'] = i.xpath('.//div[@class="info-primary"]/p/text()').extract()[1]#工作年限
    		item['education'] = i.xpath('.//div[@class="info-primary"]/p/text()').extract()[2]#学历
    		item['company_text'] = i.xpath('.//div[@class="company-text"]/p/text()').extract()[0]#公司详情
    		item['financing'] = i.xpath('.//div[@class="company-text"]/p/text()').extract()[1]#融资情况
    		#size = i.xpath('.//div[@class="company-text"]/p/text()').extract()[2]#人数
    		item['detail'] = 'https://www.zhipin.com'+i.xpath('.//h3/a/@href').get()#详情
    		yield item
    	next = response.xpath('//*[@class="page"]/a[last()]/@href').extract_first()
    	next_url = 'https://www.zhipin.com'+next
    	print(next_url)
    	if next != 'javascript:;':
    		yield scrapy.Request(url = next_url,callback=self.parse)
    	print(next_url)