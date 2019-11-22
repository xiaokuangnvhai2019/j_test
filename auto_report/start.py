from auto_report.o_mail import send_mail
from auto_report.o_report import create_report
from auto_report.setting import html_path,image_path
import os,time
from auto_report.o_data import test_product_verify
from auto_report.o_util import clear,file_list
import flask
import json

report=create_report()


server=flask.Flask(__name__) #当前Python为一个服务

@server.route("/report") #get请求，且连接带参数
def table_data():

    productid=int(flask.request.args.get("productid")) #参数名称为tablename
    projectid = int(flask.request.args.get("projectid"))

    t_time = str(int(time.time()))

    if test_product_verify(productid, projectid):

        report.test_project_bug_html(productid, projectid, t_time)
        report.test_level_bug_html(productid, projectid,t_time)
        report.test_pepole_bug_html(productid, projectid, t_time)
        report.test_verify_bug_html(productid, projectid, t_time)

        html_file_list = file_list(html_path,t_time)
        report.html_image(html_file_list)

        img_file_list = file_list(image_path,t_time)
        report.img_report(img_file_list)

        send_mail(productid,projectid)

        data = {"code": 200, "msg": "发送成功"}

        clear("report.html")


    else:
        data={"code":-2,"msg":"参数错误"}

    return  json.dumps(data,ensure_ascii=False) #返回JSON格式

server.run(host="0.0.0.0",port=5000,debug=True)