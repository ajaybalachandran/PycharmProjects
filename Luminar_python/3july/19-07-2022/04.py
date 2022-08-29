import pymysql
db = pymysql.connect(host='localhost', user='root', passwd='Meajay@1997', db='db2')
cur = db.cursor()  # object created
sql = 'select * from student2'
cur.execute(sql)
row = cur.fetchone()  # fetch only one record and store in row
print('RollNo Name')
if row:
    print(row[0], ' ', row[1])
db.commit()  # to reflect db on database
db.close()
