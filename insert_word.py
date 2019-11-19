"""

"""
import pymysql
import re
# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')
# 生成游标对象(用于操作数据库数据，获取sql执行结果的对象)
cur = db.cursor()


f = open('dict.txt');
args_list = []#[(w,m),(w,m)]
for line in f:
    # 获取单词和解释
    tup = re.findall(r"(\S+)\s+(.*)", line)[0]
    args_list.append(tup)
f.close()

sql = "insert into words (word,mean) values (%s,%s);"
try:
    cur.executemany(sql,args_list)
    db.commit()
except:
    db.commit()

#关闭游标和数据库链接
cur.close()
db.close()