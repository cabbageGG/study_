#-*- coding: utf-8 -*-

# author: li yangjin

import sqlite3, os

db_file = os.path.join(os.path.dirname(__file__),'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) PRIMARY KEY , name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
n = cursor.rowcount
print(type(n))

def get_score_in(low, high):
    # 返回指定分数区间的名字，按分数从低到高排序
    sql = 'select name from user where score>=%s and score<=%s ORDER BY score ;' % (low, high)
    print (sql)
    cursor.execute(sql)
    ret = cursor.fetchall()
    print (ret)
    ret_list = []
    for i in ret:
        ret_list.append(i[0])
    return ret_list

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
cursor.close()
conn.commit()
conn.close()

