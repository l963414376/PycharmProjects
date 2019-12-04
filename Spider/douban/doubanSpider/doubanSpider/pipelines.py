# -*- coding: utf-8 -*-

import json

import MySQLdb
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb.cursors
import MySQLdb.cursors
from scrapy import log
from twisted.enterprise import adbapi


class DoubanspiderPipeline(object):
    def __init__(self):
        self.file = open("./books.json", "wb")

    def process_item(self, item, spider):
        # 编码的转换
        for k in item:
            item[k] = item[k].encode("utf8")
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item


class MySQLPipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool("MySQLdb",
                                            db="lectures",  # 数据库名
                                            user="root",  # 数据库用户名
                                            passwd="password",  # 密码
                                            cursorclass=MySQLdb.cursors.DictCursor,
                                            charset="utf8",
                                            use_unicode=False
                                            )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tb, item):
        # tb.execute("DROP TABLE IF EXISTS douban")
        # sql = """CREATE TABLE douban (
        #                          title  CHAR(250) NOT NULL,
        #                          bd  CHAR(250),star  char(250))"""

        tb.execute("insert into douban (title, bd, star\
                       ) values (%s, %s, %s)", \
                   (item["title"], item["bd"], item["star"]))
        log.msg("Item data in db: %s" % item, level=log.DEBUG)

    def handle_error(self, e):
        log.err(e)

    # def process_item(self, item, spider):
    #     db = MySQLdb.connect("localhost", "root", "password", "lectures", charset='utf8')
    #     # 使用cursor()方法获取操作游标
    #     cursor = db.cursor()
    #
    #     # 使用execute方法执行SQL语句
    #     cursor.execute("SELECT VERSION()")
    #
    #     # 使用 fetchone() 方法获取一条数据
    #     data = cursor.fetchone()
    #
    #     print "Database version : %s " % data
    #     # 如果数据表已经存在使用 execute() 方法删除表。
    #     cursor.execute("DROP TABLE IF EXISTS shdx")
    #
    #     # 创建数据表SQL语句
    #     sql = """CREATE TABLE shdx (
    #                      lecture_name  CHAR(250) NOT NULL,
    #                      lecture_time  CHAR(20))"""
    #
    #     cursor.execute('insert into Login values(%s, %s)' % \
    #                 (item["title"], item["star"]))
    #     try:
    #         # 执行sql语句
    #         cursor.execute(sql)
    #         # 提交到数据库执行
    #         db.commit()
    #     except:
    #         # Rollback in case there is any error
    #         db.rollback()
    #
    #     #
    #     # # 关闭数据库连接
    #     # db.close()
    #     return item
