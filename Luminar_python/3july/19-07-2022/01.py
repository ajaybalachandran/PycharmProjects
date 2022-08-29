import pymysql
db = pymysql.connect(host='localhost', user='root', passwd='Meajay@1997', db='db2')
cur = db.cursor()  # object created
sql = 'select * from student2'
cur.execute(sql)
rows = cur.fetchall()
print('RollNo Name')
for i in rows:
    print(i[0], ' ', i[1])
db.commit()  # to reflect db on database
db.close()
