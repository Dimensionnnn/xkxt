import pymysql

conn = pymysql.connect(host="cdb-518aglpe.bj.tencentcdb.com", port=10101, user="root", password="zyx1999zyx",
                       database="xkxt")
cursor = conn.cursor()
sql = 'INSERT INTO student VALUES (100000, 小明, )'
cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()
