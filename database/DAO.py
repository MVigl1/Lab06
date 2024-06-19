from database.DB_connect import DBConnect as db


class DAO():
    def __init__(self):
        pass
    def populate_dd_anno(self):
        pool = db.get_connection("myPool", 3)
        pool.
