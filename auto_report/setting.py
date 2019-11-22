import  os
import nnlog

#数据库连接配置
db={
      'host':'115.28.33.230',
      'user':'root',
      'password':'123456',
      'db':'zentao',
      'port':3306
}

# num=9 #时隔天数
# startdate= '2019-11-1'  #开始时间
# enddate=time.strftime('%Y-%m-%d',time.localtime((int(time.mktime(time.strptime(startdate,'%Y-%m-%d')) )+ num * 60 * 60 * 24))) #结束时间

#邮件配置
mail_info={
      'user':'540493450@qq.com',
      'password':'lzguiofyvddrbfic',
      'host':'smtp.qq.com'}

#发送及抄送人
to='zhaowj@efreight.cn'
cc='xiaokuangnvhai@sina.com'


#路径参数配置
base_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_path=os.path.join(base_path,"auto_report/image_html")
image_path=os.path.join(base_path,"auto_report/static")
log_path=os.path.join(base_path,"auto_report/log","report.log")
wkhtmltoimage_path=r'C:\zwj\besttest\wkhtmltox\bin\wkhtmltoimage.exe'
ip="http://127.0.0.1:5000"
report_path=os.path.join(base_path,"auto_report","report.html")

#日志类
log=nnlog.Logger(log_path)



 



