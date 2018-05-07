# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import csv
class TencentPipeline(object):

    def __init__(self):
        self.f = open("tencent.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['职位名称', '职位链接', '职位类别', '人数', '工作地点', '发布时间'])


    def process_item(self, item, spider):
        tencent_list =  [item['positionName'], item['positionLink'], item['positionType'], item['peopleNumber'],item['workLocation'], item['publishTime']]
        print(tencent_list)
        self.writer.writerow(tencent_list)
        return item
    def close_spider(self, spider):#关闭
        self.writer.close()
        self.f.close()
