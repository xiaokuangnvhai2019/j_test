from auto_report.o_mail import send_mail
from auto_report.o_report import create_report
from auto_report.setting import html_path,image_path,report_path
import os,time
from auto_report.o_data import test_product_verify
from auto_report.o_util import clear,file_list
import flask
import json

report=create_report()


server=flask.Flask(__name__) #当前Python为一个服务

@server.route("/report") #get请求，且连接带参数
def table_data():

    productid=int(flask.request.args.get("productid")) #获取参数产品ID
    projectid = int(flask.request.args.get("projectid")) #获取参数项目ID

    t_time = str(int(time.time())) #获取当前时间戳，作为本次文件的唯一标识

    #判断产品及项目输入是否正确
    if test_product_verify(productid, projectid):

        report.test_project_bug_html(productid, projectid, t_time) #项目BUG状态统计表生成
        report.test_level_bug_html(productid, projectid,t_time) #项目BUG待解决BUG严重程度统计表生成
        report.test_pepole_bug_html(productid, projectid, t_time) #项目待解决BUG人员分布统计表生成
        report.test_verify_bug_html(productid, projectid, t_time) #项目已解决待验证BUG人员分布统计表成

        #生成的图表HTML转图片
        html_file_list = file_list(html_path,t_time)
        report.html_image(html_file_list)

        #图片组成报告
        img_file_list = file_list(image_path,t_time)
        report.img_report(img_file_list)

        #发送报告
        send_mail(productid,projectid)

        data = {"code": 200, "msg": "发送成功"}

        #清除本次报告report.html页面产生的数据
        clear(report_path)


    else:
        data={"code":-2,"msg":"参数错误"} #接口传参错误

    return  json.dumps(data,ensure_ascii=False) #返回JSON格式

server.run(host="0.0.0.0",port=5000,debug=True) #启动服务命令