from auto_report.setting import html_path,ip,report_path
import os
from auto_report.o_table import charts
from  auto_report.o_data import test_level_bug,test_project_bug,test_pepole_bug,test_verify_bug

b_img=charts() #声明图表类

class create_report:

    #调取图表方法，生成项目BUG状态统计表生成
    def test_project_bug_html(self,productid,projectid,t_time):
        if test_project_bug(productid,projectid):
            b_img.p_render("项目BUG状态统计情况表", test_project_bug,'test_project_bug',productid,projectid,t_time)
        else:
            return False

    # 调取图表方法，生成开发人员待解决BUG统计情况表生成
    def test_pepole_bug_html(self,productid,projectid,t_time):
        if test_pepole_bug(productid,projectid):
            b_img.p_render("项目开发人员待解决BUG统计情况表", test_pepole_bug,'test_pepole_bug',productid,projectid,t_time)
        else:
            return False

    # 调取图表方法，生成测试人员待验证BUG统计情况表生成
    def test_verify_bug_html(self,productid,projectid,t_time):
        if test_verify_bug(productid,projectid):
            b_img.line_render("项目测试人员待验证BUG统计情况表", test_verify_bug,'test_verify_bug',productid,projectid,t_time)
        else:
            return False

    # 调取图表方法，生成未解决BUG严重程度统计情况表生成
    def test_level_bug_html(self,productid,projectid,t_time):
        if test_level_bug(productid,projectid):
            b_img.pie_render("项目未解决BUG严重程度统计情况表", test_level_bug,'test_level_bug',productid,projectid,t_time)
        else:
            return False

    #获取HTML文件中文件，且生成图片
    def html_image(self,html_file_list):

        if html_file_list:
            for filename in html_file_list:
                self.new_filename=filename.replace('.html','')
                b_img.p_image(os.path.join(html_path,filename),self.new_filename)
        else:
            return False

    #获取图片文件中的图片，且生成report文件
    def img_report(self,img_file_list):
        if img_file_list:
            for img in img_file_list:
                self.f=open(report_path,"a+",encoding='utf-8')
                html='''<div><img src="%s/static/%s"></div>'''%(ip,img)
                self.f.write(html)
                self.f.close()
        else:
            return False



