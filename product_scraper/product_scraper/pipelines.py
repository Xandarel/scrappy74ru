from ciber_sec_test.product_scraper.connector import db_connect
from psycopg2 import sql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class DataTable():
    def insert(self, con, value):
        # print('Start insert')
        # con.autocommit = False
        values = (con.pos, value['url'], value['title'], value['text'])
        # print(values)
        con.cur.execute("INSERT INTO articles (id, url, title, text) VALUES (%s,%s,%s,%s);", values)
        con.pos += 1
        con.con.commit()


class ProductScraperPipeline:
    def process_item(self, item, spider):
        item['text'] = ' '.join(item['text'])
        dt = DataTable()
        dt.insert(db_connect, item)
        # print('HERE')
        return item
