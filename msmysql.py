import MySQLdb

class Msmysql:
    '''
    class of deal mysql data. base pyhton3.x MySQLdb
    '''
    
    def __init__(self, dbhost="localhost", dbuser="root", dbpwd="", dbname="testdb", char='utf8'):
        self.db = MySQLdb.connect(dbhost, dbuser, dbpwd, dbname, charset=char)
        self.cursor = None

    # 获取多行数据
    def selectAll(self,sql):
        if not sql: return None
        self.getCursor(1) # 获取操作游标
        self.cursor.execute(sql) # 执行SQL语句
        result = self.cursor.fetchall() # 使用 fetchone() 方法获取一条数据
        return result
        return list(result)

    # 获取一行数据
    def selectOne(self,sql):
        if not sql: return None
        self.getCursor(1) # 获取操作游标
        self.cursor.execute(sql) # 执行SQL语句
        return self.cursor.fetchone() # 获取一条数据

    # 插入数据
    def doInsert(self,sql):
        return self.doUpdate(sql)

    # 更新数据
    def doUpdate(self,sql):
        if not sql: return None
        self.getCursor() # 获取操作游标
        self.doQuery(sql) # 执行SQL语句
        return self.cursor.rowcount # 返回影响的行数。

    # 获取操作游标
    def getCursor(self,type=0):
        if type:
            # 使用字典结果
            self.cursor=self.db.cursor(cursorclass = MySQLdb.cursors.DictCursor);
        else:
            self.cursor=self.db.cursor()

    # 执行sql语句
    def doQuery(self,sql):
        try:
           self.cursor.execute(sql) # 执行SQL语句
           self.db.commit() # 提交到数据库执行
        except:
           self.db.rollback() # 发生错误时回滚

    def __del__(self):
        self.cursor.close() # 关闭cursor
        self.db.close() # 关闭数据库连接



if __name__ == '__main__':
    sql = 'SELECT m_time,m_author,m_title FROM `ms_news`'
    m = Msmysql()
    for line in m.selectAll(sql):
        print(line['m_time'], line['m_author'], line['m_title'])
