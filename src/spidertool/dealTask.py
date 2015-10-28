#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime
import time
import connectpool
from TaskTool import TaskTool
import SQLTool
class dealTask(TaskTool):
	def __init__(self):
		TaskTool.__init__(self)
		self.connectpool=connectpool.ConnectPool()
	def task(self,req,threadname):
		print threadname+'执行任务中'+str(datetime.datetime.now())
		ans = req[0];

		print threadname+'任务结束'+str(datetime.datetime.now())
		return ans

if __name__ == "__main__":
	DealSQL=SQLTool.DBmanager()
	DealSQL.connectdb()
	(result,title,count,col)=DealSQL.searchtableinfo_byparams(['webdata'],['address','content','meettime'])
	DealSQL.closedb()
	#TODO 添加元组进去
	#ｕｒｌ也要存进去
	f = dealTask()
	f.set_deal_num(10)


	for data in result:
		f.add_work([(data[0],data[1])])
#		print data[1]

	f.start_task()
	while f.has_work_left():
		v,ans=f.get_finish_work()
		print ans
	while True:
		pass



