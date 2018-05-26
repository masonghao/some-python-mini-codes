# * 1. 连接mysql数据库获取数据
# * 2. 重命名文件夹下全部文件名


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


'''
2. 重命名文件夹下全部文件名
  changeFileName.py ------------------------------------------------------------ start
'''
import os
path='./somefiles'; #要管理的文件夹名字
count=0;
filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
def rename():
    global count
    for files in filelist:#遍历所有文件
        Olddir=os.path.join(path,files);#原来的文件路径
        filename=os.path.splitext(files)[0];#文件名
        filetype=os.path.splitext(files)[1];#文件扩展名
        Newdir=os.path.join(path,str(count)+filetype);#新的文件路径，这一行可以根据需要进行修改
        os.rename(Olddir,Newdir);#重命名
        count+=1;
rename();
'''
  changeFileName.py ------------------------------------------------------------ end
'''
