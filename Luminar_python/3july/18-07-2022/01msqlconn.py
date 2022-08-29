import pymysql
db = pymysql.connect(host='localhost', user='root', passwd='Meajay@1997', db='db2')
cur = db.cursor()  # object created
sql = '''update student2 set class= 12 where roll_no=1'''
cur.execute(sql)
db.commit()  # to reflect db on database
db.close()
