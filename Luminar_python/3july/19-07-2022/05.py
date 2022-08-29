import pymysql
db = pymysql.connect(host='localhost', user='root', passwd='Meajay@1997', db='db2')
cur = db.cursor()  # object created
sql = 'select name from student2'
cur.execute(sql)
print('No of rows=', cur.rowcount)
db.close()
