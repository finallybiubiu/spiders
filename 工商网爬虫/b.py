#encoding:utf-8
from pyquery import PyQuery as pq
import time
import re
import urllib, urllib2, httplib

url_front='http://tjcredit.gov.cn'
url_end='&departmentId=scjgw&infoClassId=dj'
url_root = 'http://tjcredit.gov.cn/platform/saic/exclist.ftl?Page=' 
list3=[]
def _test_url_(url):
	statusCode =urllib2.urlopen(url).getcode()
	return statusCode==200

def _parse_info_(url):
	dic={}
	list1=[]
	list2=[]	
	# print '666666666666666666666666666666'	
	if _test_url_(url)==True:
		# print '666666666666666666666666666666'
		response=urllib2.urlopen(url)
		html=response.read().decode('utf-8')
		print html
		# doc=pq(url='http://qyxy.baic.gov.cn/yzwfqymd/yzwfqymdAction!ccxxquery.dhtml?clear=true#')
		#doc=pq(url='http://tjcredit.gov.cn/platform/saic/baseInfo.json?entId=00015c3b53ee8a284a1017f900ce054b&departmentId=scjgw&infoClassId=dj')
		doc=pq(unicode(html))
		data=doc('table.result-table')
		table1= pq(data).eq(0).html()
		print table1
		a=pq(table1)
		data1=a('td')
		info=''
		num=0
		for i in data1:
			table2=pq(i).text()
			if(table2=='登记状态'.decode('utf-8')):
				break;
			info=info+table2+','
			print table2
		print('****************************8')

		list1 = info.split(',')
		listinfo = list1[1:-1]
		print len(listinfo)
		for i in range(len(listinfo)/2):
			list3.append(listinfo[i*2])
			print i
			print listinfo[i*2]
			print listinfo[i*2+1]
			dic[listinfo[i*2]]=listinfo[i*2+1]
		print dic
	else:
		print 'NET  ERROR'

class UrlParser():
	def __init__(self):
		self.urls = []
	def feed(self,data):
		url = re.findall(r'''<a(\s*)(.*?)(\s*)href(\s*)=(\s*)([\"\s]*)([^\"\']+?)([\"\s]+)(.*?)>''',data,re.S|re.I)
		for u in url:
			if len(u[6])>len('http://gsxt.saic.gov.cn/'):
				self.urls.append(u[6])
	def geturls(self):
		return self.urls

def _spider_range_(a,b):
	urls = []
	for i in range(a,b):
		# print '+++++++++++++++++++++++++++++++++++'
		url1=url_root+str(i)
		response=urllib2.urlopen(url1)
		html=response.read().decode('utf-8')
		url = UrlParser()
		url.feed(html)
		urls += url.geturls()
		# print urls
	print urls
	return urls

def _spider_action_(urls):	
	for i in range(1,len(urls)):
		pa = re.compile('/viewBaseExc.ftl?')
		newurl=pa.sub('/baseInfo.json',urls[i])
		wurl =url_front+newurl+url_end
		print wurl
		_parse_info_(wurl)

if __name__ == '__main__':	
	urls1 = _spider_range_(1,20)
	_spider_action_(urls1)
	print list(set(list3))
	
