#### Ubuntu配置ssh，允许使用用户名外部访问，允许stfp传输文件

###### #安装ssh

​	sudo apt-get install openssh-server

###### #查看ssh服务状态

​	ps -aux|grep sshd

###### #修改sshd配置文件

​	sudo vi /etc/ssh/sshd_config

​		 28 #PermitRootLogin prohibit-password
​		 29 PermitRootLogin yes 

 		78 Subsystem sftp internal-sftp

###### #重启服务

​	sudo service sshd restart 



#### 异步消息队列celery的使用

###### #安装celery

​	$ pip install celery

​	使用redis作为celery的broker

​	$ pip install celery-with-redis

###### #编写任务 tasks.py

​	import time
​	from celery import Celery

​	celery = Celery('tasks', broker='redis://localhost:6379/0')

​	@celery.task
​	def sendmail(mail):
​    	print('sending mail to %s...' % mail['to'])
   	 time.sleep(2.0)
   	 print('mail sent.')

###### #启动celery处理任务

​	$ celery -A 文件名 worker --loglevel=info

###### #后台以守护进程的方式启动celery

​	$ celery multi start w1 -A 文件名 -l info --logfile=celerylog.log --pidfile=celerypid.pid

​	动态查看日志

​	$ tail -100f celerylog.log

###### #测试异步任务

​	使用celery所在的python环境

​	$ python3.6

​	>>> from tasks import sendmail 

​	>>> sendmail.delay("123@456.mail")