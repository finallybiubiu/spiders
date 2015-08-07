#encoding:utf-8
from pyquery import PyQuery as pq
import time
import re
import urllib, urllib2, httplib
import MySQLdb

list3=['注册号', '成立日期', '法定代表人','负责人','投资人', '经营者', '注册资本', '组成形式','经营场所', '住所','营业场所','经营范围',  '注册日期', '类型', 
'经营期限至', '经营期限自', '营业期限至', 
 '核准日期', '登记机关', '营业期限自',   ]
# list3=['负责人','登记机关']
conn= MySQLdb.connect(
	host='localhost',
	port = 3306,
	user='root',
	passwd='root',
	db ='test',
	charset='utf8',
	)
cur = conn.cursor()
cur.execute("create table tianjin (名称  varchar(300))")
cur.execute("alter table tianjin add primary key(名称)")
for i in range(len(list3)):
	string="alter table tianjin add "+list3[i]+" varchar(200)"
	print string
	cur.execute(string)


