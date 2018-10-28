# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ZhipinPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    def __init__(self,host,port,user,password,database):
        self.host = host
        self.database = database,
        self.user = user
        self.password = password
        self.port = port,





    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            host = crawler.settings.get('MYSQL_HOST'),
            database = crawler.settings.get('MYSQL_DATABASE'),
            user = crawler.settings.get('MYSQL_USER'),
            password  = crawler.settings.get('MYSQL_PASSWORD'),
            port = crawler.settings.get('MYSQL_PORT'),
        )
    def open_spider(self,spider):
        self.db = pymysql.connect(self.host,self.user,self.password,
                                  self.database,port = self.port,charset = 'utf8')
        self.cursor = self.db.cursor()

    def close_spider(self):
        self.db.close()

    def process_item(self,item,spider):
        data = dict(item)
        keys = ','.join(data.keys())
        values = ','.join(['%s']*len(data))
        sql = 'insert into book_booktest(%s) values (%s)'%(keys,values)
        self.cursor.execute(sql)
        self.db.commit()
        return item
