import psycopg2


class DB_connector():
    def __init__(self):
        self.con = psycopg2.connect(dbname='test', user='postgres', password='1', host='localhost')
        self.cur = self.con.cursor()
        self.pos = 1


db_connect = DB_connector()
