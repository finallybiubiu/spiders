#encoding:utf-8
from pyquery import PyQuery as pq
import time
import re
import urllib, urllib2, httplib
import MySQLdb

list3=['注册号', '成立日期', '法定代表人','负责人','投资人', '经营者', '注册资本', '组成形式','经营场所', '住所','营业场所','经营范围',  '注册日期', '类型', 
'经营期限至', '经营期限自', '营业期限至', 
 '核准日期', '登记机关', '营业期限自', '变更事项','变更前内容','变更后内容','变更日期'  ]
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
# cur.execute('insert into tinajin (名称) value (天津综合商店)')
# cur.execute('select * from tianjin where 名称 = '+name.encode('utf-8'))
# cur.execute("update tianjin set 经营范围='中成药、化学药制剂、抗生素、生化药品零售；III类：一次性注射器、输液器；II类：普通诊察仪器；II类：医用卫生材料及敷料;II:类：物理治疗及康复仪器；II类：中医器械；II类：临床检验分析仪器及配套试纸；II类：医用制气设备；II类：避孕器械；II类：导管、引流管；I类：基础外科手术器械；I类：医用供气、输气装置；I类:医用冷敷器具；I类：一般医疗用品零售。（国家有专项专营规定的按规定执行；涉及行政许可的凭许可证或批准文件经营）' where 名称='天津市西青区聚济堂大药房'")
cur.execute("create table tianjin (名称  varchar(40))")
cur.execute("alter table tianjin add primary key(名称)")
for i in range(len(list3)):
	string="alter table tianjin add "+list3[i]+" varchar(40)"
	print string
	cur.execute(string)


