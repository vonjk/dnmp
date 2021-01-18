#coding:utf-8
import time

# http://foreversong.cn/archives/1263

#mysql log位置
file = './data/mysql/mysql.log'

#去重函数
def removal(string):
	log_list_new = []
	num = string[:2]
	log_list = string.split(num)
	for i in log_list:
		i = i.rstrip('\t').rstrip()
		log_list_new.append(i)
	log_list_new = list(set(log_list_new))
	string = num + ' '
	for j in log_list_new:
		string += j 
	return string

#获取当前时间函数
def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

#监控日志文件函数
def monitorLog(logFile):
  print '监控的日志文件是  %s' % logFile
  print '当前时间是  %s' % GetNowTime() 
  with open(file , 'r') as fp:
    fp.seek(0,2)
    try:
      while True:
        last_pos = fp.tell()
        line = fp.readline().strip()
        #这里只读取预编译和执行语句
        if ('Prepare' in line) or ('Execute' in line) or ('Query' in line):
          print removal(line)
          print '--------------------------------------------------------------------------------------------------------------------'
    except KeyboardInterrupt:
      print 'exit...'

        	
if __name__ == '__main__':
    monitorLog(file)