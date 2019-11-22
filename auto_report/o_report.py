from auto_report.setting import html_path
import os
from auto_report.o_table import charts
from  auto_report.o_data import test_level_bug,test_project_bug,test_pepole_bug,test_verify_bug

b_img=charts()

class create_report:

    def test_project_bug_html(self,productid,projectid,t_time):
        if test_project_bug(productid,projectid):
            b_img.p_render("项目BUG状态统计情况表", test_project_bug,'test_project_bug',productid,projectid,t_time)
        else:
            return False

    def test_pepole_bug_html(self,productid,projectid,t_time):
        if test_pepole_bug(productid,projectid):
            b_img.p_render("项目开发人员待解决BUG统计情况表", test_pepole_bug,'test_pepole_bug',productid,projectid,t_time)
        else:
            return False

    def test_verify_bug_html(self,productid,projectid,t_time):
        if test_verify_bug(productid,projectid):
            b_img.line_render("项目测试人员待验证BUG统计情况表", test_verify_bug,'test_verify_bug',productid,projectid,t_time)
        else:
            return False

    def test_level_bug_html(self,productid,projectid,t_time):
        if test_level_bug(productid,projectid):
            b_img.pie_render("项目未解决BUG严重程度统计情况表", test_level_bug,'test_level_bug',productid,projectid,t_time)
        else:
            return False


    def html_image(self,html_file_list):

        if html_file_list:
            for filename in html_file_list:
                self.new_filename=filename.replace('.html','')
                b_img.p_image(os.path.join(html_path,filename),self.new_filename)
        else:
            return False

    def img_report(self,img_file_list):
        if img_file_list:
            for img in img_file_list:
                self.f=open("report.html","a+",encoding='utf-8')
                html='''<div><img src="http://127.0.0.1:5000/static/%s"></div>'''%img
                self.f.write(html)
                self.f.close()
        else:
            return False



