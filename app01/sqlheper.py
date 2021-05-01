import pymysql

def get_list(sql,args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='cjly', passwd='cjly0915', db='django')
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 执行SQL，并返回受影响函数
    cursor.execute(sql,args)
    result = cursor.fetchall()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return result

def get_one(sql,args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='cjly', passwd='cjly0915', db='django')
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 执行SQL，并返回受影响函数
    cursor.execute(sql,args)
    result = cursor.fetchone()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return result

def modify(sql,args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='cjly', passwd='cjly0915', db='django')
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 执行SQL，并返回受影响函数
    cursor.execute(sql, args)
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

def create(sql,args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='cjly', passwd='cjly0915', db='django')
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 执行SQL，并返回受影响函数
    cursor.execute(sql, args)
    conn.commit()
    last_row_id = cursor.lastrowid
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return last_row_id

class SqlHelper(object):
    def __init__(self):
        #读取配置文件
        self.connnect()
    def connnect(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='cjly', passwd='cjly0915', db='django')
        # 创建游标
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_list(self,sql,args):
        # 执行SQL，并返回受影响函数
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        return result

    def get_one(self, sql, args):
        # 执行SQL，并返回受影响函数
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result

    def modify(self,sql,args):
        self.cursor.execute(sql, args)
        self.conn.commit()

    def multiple_modify(self,sql,args):
        # self.cursor.executemany('insert into bd(id,name) values(%s,%s)'[(1,'alex'),(2,'eric')])
        self.cursor.executemany(sql,args)
        self.conn.commit()

    def create(self,sql,args):
        self.cursor.execute(sql, args)
        self.conn.commit()
        return self.cursor.lastrowid

    def close(self):
        self.cursor.close()
        self.conn.close()

