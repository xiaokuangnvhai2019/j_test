import yagmail
import traceback
from auto_report.setting import mail_info,to,cc,log
from auto_report.o_data import sql_pakeage,test_projectname,connect_db
from auto_report.o_util import read_file


#发送邮件
def send_mail(productid,projectid):

    bug_sql=sql_pakeage(productid,projectid)

    bug_num=[]

    for sql in bug_sql:
        bug_num.append(int(connect_db(sql)[0]))

    project_name=test_projectname(projectid)

    subject="%s项目测试报告"%project_name

    str='''<div style="color:#000; font-size: 14px;font-family: arial;"> <span style="font-family: 微软雅黑, Microsoft YaHei; font-size: 16px;">大家好：</span></div><div style="color:#000; font-size: 14px;font-family: arial;">
    <span style="font-family: 微软雅黑, Microsoft YaHei; font-size: 16px;">
    &nbsp;&nbsp;&nbsp;&nbsp;​&nbsp;&nbsp;&nbsp;&nbsp;​&nbsp;&nbsp;&nbsp;&nbsp;​%s项目，目前存在%s个BUG，已解决状态%s个BUG，未解决状态%s个BUG，延期处理状态%s个BUG，已关闭状态%s个BUG；请对应开发注意查收及修改自己名下的BUG。</span></div><div style="color:#000; 
    font-size: 14px;font-family: arial;"><br></div><div style="color:#000; font-size: 14px;font-family: arial;">
    <span style="font-family: 微软雅黑, Microsoft YaHei; font-size: 16px;">​各维度测试情况统计如下图：</span><div><br></div></div>'''%(project_name,bug_num[0],bug_num[1],bug_num[2],bug_num[3],bug_num[4])


    file_content=read_file("./report.html")

    content=str+file_content


    try:
        mail = yagmail.SMTP(**mail_info)  # 解包方式传入参数
        mail.send(to=to, cc=cc, subject=subject, contents=content)  # 发送邮件

    except Exception as e:
        log.error("发送邮件出错了，错误信息是：\n%s" % traceback.format_exc())  # 捕获错误信息

    else:
        log.info("发送邮件成功")  # 发送成功日志

