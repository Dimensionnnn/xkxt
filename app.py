import pymysql


conn = pymysql.connect(host="cdb-518aglpe.bj.tencentcdb.com", port=10101, user="root", password="zyx1999zyx", database="xkxt")
cursor = conn.cursor()  
sql = 'ALTER TABLE `sc` ADD PRIMARY KEY USING BTREE (`cno`,`sno`)'
cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()