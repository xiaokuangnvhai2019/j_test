import  os
import nnlog


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


mail_info={
      'user':'540493450@qq.com',
      'password':'lzguiofyvddrbfic',
      'host':'smtp.qq.com'}


to='zhaowj@efreight.cn'
cc='xiaokuangnvhai@sina.com'



base_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_path=os.path.join(base_path,"image_html")
image_path=os.path.join(base_path,"static")
log_path=os.path.join(base_path,"log","report.log")
wkhtmltoimage_path=r'C:\zwj\besttest\wkhtmltox\bin\wkhtmltoimage.exe'

log=nnlog.Logger(log_path)



 



