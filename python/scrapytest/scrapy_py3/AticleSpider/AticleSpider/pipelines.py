# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import MySQLdb, json, MySQLdb.cursors
import codecs
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi


class AticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class AticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        if 'front_image_url' in item:
            for ok, value in results:
                image_file_path = value['path']
            item['front_image_path'] = image_file_path

        return item


class JsonFilePipeline(object):
    #自定义json文件的导出
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    def close_spider(self, spider):
        print('close')
        self.file.close()

class JsonExporterPipleline(object):
    #调用scrapy提供的json export导出json文件
    def __init__(self):
        self.file = open('articleexport.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):  #关闭spider时会调用
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item



class mysqlPipeline(object):
    # 自定义同步mysql写入
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'dev', '123456', 'scrapy', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):
        sql = 'insert into article_spider (url_id,title,front_image_url,content,create_date,fav_nums,praise_nums,comment_nums,tags,url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        self.cursor.execute(sql, (item['url_id'],item['title'],item['front_image_url'],item['content'],item['create_date'],item['fav_nums'],item['praise_nums'],item['comment_nums'],item['tags'],item['url']))
        self.conn.commit()
        return item

class MysqlTwistedPipline(object):
    # scrapy 异步mysql导入
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host = settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd = settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        return cls(dbpool)

    def process_item(self, item, spider):
        #使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider) #处理异常

    def handle_error(self, failure, item, spider):
        #处理异步插入的异常
        print (failure)

    def do_insert(self, cursor, item):
        #执行具体的插入
        #根据不同的item 构建不同的sql语句并插入到mysql中
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)



