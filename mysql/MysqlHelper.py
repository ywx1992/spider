import pymysql


class MysqlHelper(object):
    def __init__(self, host, port, db, user, password, charset='utf8'):
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, password=password, charset=charset)

    def get_one(self, sql, params=[]):
        try:
            cur = self.conn.cursor()
            cur.execute(sql, params)
            result = cur.fetchone()
            cur.close()
            self.conn.close()
            return result
        except Exception as e:
            print(e)

    def get_all(self, sql, params=[]):
        try:
            cur = self.conn.cursor()
            cur.execute(sql, params)
            result = cur.fetchall()
            cur.close()
            self.conn.close()
            return result
        except Exception as e:
            print(e)

    def insert(self, sql, params=[]):
        return self.__cud(sql, params)

    def update(self, sql, params=[]):
        return self.__cud(sql, params)

    def delete(self, sql, params=[]):
        return self.__cud(sql, params)

    def __cud(self, sql, params=[]):
        try:
            cur = self.conn.cursor()
            count = cur.execute(sql, params)
            self.conn.commit()
            cur.close()
            self.conn.close()
            return count
        except Exception as e:
            print(e)
            self.conn.rollback()


