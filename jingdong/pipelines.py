# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JingdongPipeline(object):
    def process_item(self, item, spider):
        db = pymysql.connect(host="127.0.0.1", user="root", password="zb876231", db="pythondata", charset="utf8")
        cursor = db.cursor()
        if (len(price) and len(comment) and len(rate) and len(name1) and len(shopname1)):
            sql = "insert into jd(name,price,shopname,com,rate,url) values(%s,%s,%s,%s,%s,%s)"
            data = (name1, price[0], shopname1, comment[0], rate[0], url)
            cursor.execute(sql, data)
        else:
            pass
        db.commit()
