# * 1. 连接mysql数据库获取数据


'''
1. 连接mysql数据库获取数据
  mysqlLib.py ------------------------------------------------------------------start
'''
# -*- coding: UTF-8 -*-
"""
连接mysql数据库获取数据
"""
import MySQLdb
def get_list(sql = 'SELECT m_time,m_title FROM `ms_news`'):
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "", "msbooks", charset='utf8' )
    cursor = db.cursor() # 使用cursor()方法获取操作游标 
    cursor.execute(sql) # 使用execute方法执行SQL语句
    data = cursor.fetchall() # 使用 fetchone() 方法获取一条数据
    # 关闭数据库连接
    db.close()
    return data

if __name__ == '__main__':
    sql = 'SELECT m_time,m_author,m_title FROM `ms_news`'
    for x in get_list(sql):
        print(*x)
'''
  mysqlLib.py ------------------------------------------------------------------ end
'''
