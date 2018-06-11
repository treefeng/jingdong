# -*- coding: utf-8 -*-
import scrapy
from jingdong.items import JingdongItem
import re
import pymysql
import urllib.request
from scrapy.http.request import Request
import random


class JdspSpider(scrapy.Spider):
    name = "jdsp"
    allowed_domains = ["http://www.jd.com"]
    def start_requests(self):
            for i in range(1,105):
                url="https://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
                yield Request(url,callback=self.parse)
    def parse(self, response):
        item=JingdongItem()
        id=response.xpath('//div[@class="gl-i-wrap j-sku-item"]/@data-sku').extract()
        item['name']=response.xpath('//a[@target="_blank"][@title=""]/em/text()').extract()
        item['shopname']=response.xpath('//div[@class="p-shop"]/@data-shop_name').extract()
        '''for item_id in (id):
            url1="https://p.3.cn/prices/mgets?callback=jQuery6324226&type=1&area=1_72_4137_0&skuIds=J_"+item_id
            url2 = "http://club.jd.com/comment/productCommentSummaries.action?my=pinglun2&referenceIds=" + item_id
            pat1='"p":"(.*?)"'
            pat2='"CommentCount":(.*?),"'
            pat3='"GoodRate":(.*?),"'
            price=re.compile(pat1).findall(urllib.request.urlopen(url1).read().decode("GBK","ignore"))
            comment=re.compile(pat2).findall(urllib.request.urlopen(url2).read().decode("GBK","ignore"))
            rate=re.compile(pat3).findall(urllib.request.urlopen(url2).read().decode("GBK","ignore"))
            url="//item.jd.com/"+item_id+".html"
            price_list=[]
            comment_list=[]
            rate_list=[]
            url_list=[]
            price_list.append(price)
            comment_list.append(comment)
            rate_list.append(rate)
            url_list.append(url)
        print(price_list)'''
        print(item)
        return item



