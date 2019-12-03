# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ShdxxsbgspiderPipeline(object):
    def process_item(self, item, spider):
        data = ''
        with open ('lecture.txt','w',enconding = 'utf-8') as f:
            names = item['name']
            times = item['time']
            for i,j in zip(names,times):
                data += i + ':' + j +'\n'
                f.write()
                f.close()
        return item
