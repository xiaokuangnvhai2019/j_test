from pyecharts import Bar
from pyecharts import Pie
from pyecharts import Line
from auto_report.setting import html_path,image_path,wkhtmltoimage_path
import  imgkit
import os

class charts:

    #柱状图
    def p_render(self,render_name,mothed_name,name,productid,projectid,t_time):
        bar = Bar(render_name)
        bar.add('',list(mothed_name(productid,projectid).keys()),list(mothed_name(productid,projectid).values()),is_label_show=True,is_toolbox_show=False)
        bar.render(path=os.path.join(html_path,"%s_%s.html"%(name,t_time)))


    # #横线柱状图
    # def p_xy_render(self,render_name,mothed_name,name,productid,projectid,t_time):
    #     bar = Bar(render_name)
    #     bar.add('',list(mothed_name(productid,projectid).keys()),list(mothed_name(productid,projectid).values()),is_label_show=True,is_toolbox_show=False,is_convert=True,yaxis_interval=0)
    #     bar.render(path=os.path.join(html_path,"%s_%s.html"%(name,t_time)))

    #饼图图
    def pie_render(self,render_name,mothed_name,name,productid,projectid,t_time) :

        pie =Pie(render_name,is_animation=False)
        pie.add("",list(mothed_name(productid,projectid).keys()),list(mothed_name(productid,projectid).values()), is_label_show=True,is_toolbox_show=False)
        pie.show_config()
        pie.render(path=os.path.join(html_path,"%s_%s.html"%(name,t_time)))

    #线形图
    def line_render(self,render_name,mothed_name,name,productid,projectid,t_time):

        line = Line(render_name)
        line.add('', list(mothed_name(productid,projectid).keys()),list(mothed_name(productid,projectid).values()),is_label_show=True,is_toolbox_show=False)
        line.render(path=os.path.join(html_path,"%s_%s.html"%(name,t_time)))

    #HTML生成图片
    def p_image(self,html,imagename):
        self.confg = imgkit.config(wkhtmltoimage=wkhtmltoimage_path)  # 声明wkhtmltopdf地址
        imgkit.from_file(html,os.path.join(image_path,"%s.jpg"%imagename),config=self.confg)


