#-*- coding: utf-8 -*-

# author: li yangjin

import MySQLdb
"""
    MYSQL:用法
        host
          string, host to connect

        user
          string, user to connect as

        passwd
          string, password to use

        db
          string, database to use

        port
          integer, TCP/IP port to connect to
"""
conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="123456",db="test",port=3306)
cursor = conn.cursor()
# cursor.execute('create table user1(id varchar(20) PRIMARY KEY , name varchar(20), score int)')
cursor.execute(r"insert into user1 values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user1 values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user1 values ('A-003', 'Lisa', 78)")
conn.commit()

def get_score_in(low, high):
    # 返回指定分数区间的名字，按分数从低到高排序
    sql = 'select name from user1 where score>=%s and score<=%s ORDER BY score ;' % (low, high)
    print (sql)
    cursor.execute(sql)
    ret = cursor.fetchall()
    print (ret)
    return [i[0] for i in ret]

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
cursor.close()
conn.close()



