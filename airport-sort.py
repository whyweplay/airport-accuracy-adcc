#访问数据库
import pymysql
connect=pymysql.Connect(
host='localhost',
port=3306,
user='root',
passwd='password',
db='mydata',
charset='utf8'
)
cursor=connect.cursor()
sql1='SELECT r_depap FROM fme_archive_today WHERE executedate between 20180101 and 20180120'
sql2='SELECT r_arrap FROM fme_archive_today WHERE executedate between 20180101 and 20180120'
cursor.execute(sql1)
cursor.execute(sql2)
result=cursor.fetchall()
myset=set(result)
list1=[]
for item in myset:
	list1.append(result.count(item))
	print('the %s has found %d'%(item,result.count(item)))
print(sorted(list1,reverse=True))
cursor.close()
connect.close() 

