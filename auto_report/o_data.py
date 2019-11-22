import pymysql
from  auto_report.o_util import spread,list_dic
from  auto_report.setting import db


#建立数据库连接及执行
def connect_db(sql):
    conn = pymysql.connect( **db,charset='utf8',
                           autocommit=True)
    cur = conn.cursor()  # 建立游标
    sql = sql
    cur.execute(sql)
    r_result =spread(cur.fetchall())
    cur.close()
    conn.close()
    return r_result


#BUG状态统计SQL封装
def sql_pakeage(productid,projectid):

    bug_sql = "select count(*) from zt_bug where product='%d' and project='%d' and deleted='0'"% (
    productid, projectid)

    resolved_bug_sql = "select count(*) from zt_bug where product = '%d' and project='%d' and deleted = '0' and `status` = 'resolved' and resolution <> 'postponed' " % (
        productid, projectid)

    not_resolved_bug_sql = "select count(*) from zt_bug where product = '%d' and project='%d' and deleted = '0' and `status` =  'active' " % (
        productid, projectid)

    postponed_bug_sql = "select count(*) from zt_bug where product = '%d' and project='%d' and deleted = '0' and `status` <> 'closed' and resolution = 'postponed' " % (
        productid, projectid)

    closed_bug_sql = "select count(*) from zt_bug where product='%d'and project='%d' and deleted = '0' and `status` = 'closed' " % (
        productid, projectid)

    return  bug_sql,resolved_bug_sql,not_resolved_bug_sql,postponed_bug_sql,closed_bug_sql



#总的项目BUG情况统计
def  test_project_bug(productid,projectid):

    #总bug数
    all_bug=connect_db(sql_pakeage(productid,projectid)[0])

    #已解决bug数
    resolved_bug = connect_db(sql_pakeage(productid,projectid)[1])

    # 未解决BUG数（当前显示BUG状态为未解决的。包含当前还没被解决的、之前遗留的未解决、以及reopen的BUG（累计数据））
    not_resolved_bug =  connect_db(sql_pakeage(productid,projectid)[2])

    # 延期BUG数
    postponed_bug= connect_db( sql_pakeage(productid,projectid)[3])

    # 已关闭BUG数
    closed_bug = connect_db(sql_pakeage(productid,projectid)[4])

    statistics_bug = { "总BUG数":all_bug[0],"已解决BUG": resolved_bug[0], "未解决BUG": not_resolved_bug[0], "已关闭BUG": closed_bug[0],
                      "延期解决BUG": postponed_bug[0]}

    return  statistics_bug



#未解决及待验证BUG人均分布
def test_pepole_bug(productid,projectid):

    #未解决BUG分布sql
    not_resolved_sql="select assignedTo,count(*) from zt_bug where product = '%d' and project='%d' and deleted = '0' and `status` =  'active' and assignedTo <> 'closed'  group by assignedTo"%(productid,projectid)

    # 未解决BUG分布
    not_resolved_bug=connect_db(not_resolved_sql)


    return list_dic(not_resolved_bug)



#未解决BUG严重程度统计
def test_level_bug(productid,projectid):

     level_bug_sql="select severity,count(*) from zt_bug where product ='%d' and project='%d' and deleted = '0' and `status` =  'active' and assignedTo <> 'closed'  group by severity"%(productid,projectid)

     level_bug=connect_db(level_bug_sql)

     return list_dic(level_bug)


#已解决待验证BUG分布
def test_verify_bug(productid,projectid):

       #已解决待验证BUG分布sql
       not_verify_sql="select assignedTo,count(*) from zt_bug where product = '%d' and project='%d' and deleted = '0' and `status` ='resolved'  and resolution='fixed' group by assignedTo"%(productid,projectid)
       # 已解决待验证BUG分布
       not_verify_bug = connect_db(not_verify_sql)

       return    list_dic(not_verify_bug)


def test_projectname(projectid):
    projectname="select `name` from zt_project where id='%d'"%(projectid)
    return connect_db(projectname)[0]

#验证项目名称及产品名称是否存在及是对应关系
def test_product_verify(productid,projectid):
    if productid:
        p_sql = "select project from zt_projectproduct where product=%d" % productid
        projectlist=connect_db(p_sql)

        if projectid & projectid in projectlist:

            return True

        else:
            return False

    else:
        return False





#带时间的参数
#    bug_sql="select count(*) from zt_bug where product='%d' and project='%d' and deleted='0' and activatedCount='0' and openedDate >= '%s' and openedDate <= '%s' "%(productid,projectid,startdate,enddate)
#
#     resolved_bug_sql="select count(*) from zt_bug where product = '%d' and project='%d' and deleted = '0' and `status` <> 'active' and resolution <> 'postponed' and resolvedDate >= '%s' and resolvedDate <= '%s'" %(
# productid,projectid, startdate, enddate)
#
#     not_resolved_bug_sql="select count(*) from zt_bug where product = '%d' and project='%d' and deleted = '0' and `status` =  'active' and openedDate <= '%s'" %(
# productid,projectid, enddate)
#
#     postponed_bug_sql="select count(*) from zt_bug where product = '%d' and project='%d' and deleted = '0' and `status` <> 'closed' and resolution = 'postponed' and resolvedDate <= '%s'"%(
# productid, projectid,enddate)
#
#     closed_bug_sql="select count(*) from zt_bug where product='%d'and project='%d' and deleted = '0' and `status` = 'closed' and closedDate >= '%s' and closedDate <= '%s'"% (
# productid, projectid,startdate,enddate)



#以设定时间进行查询各状态BUG数
# def  time_bug():
#
#     #新增BUG数
#     new_bug=connect_db(sql_pakeage()[0])
#
#     #已解决bug数
#     resolved_bug = connect_db(sql_pakeage()[1])
#
#     # 未解决BUG数（当前显示BUG状态为未解决的。包含当前还没被解决的、之前遗留的未解决、以及reopen的BUG（累计数据））
#     not_resolved_bug =  connect_db(sql_pakeage()[2])
#
#     # 延期BUG数
#     postponed_bug= connect_db(sql_pakeage()[3] )
#
#     # 已关闭BUG数
#     closed_bug = connect_db(sql_pakeage()[4] )
#
#     statistics_bug = {'新增BUG': new_bug[0], "已解决BUG": resolved_bug[0], "未解决BUG": not_resolved_bug[0], "已关闭BUG": closed_bug[0],
#                       "延期解决BUG": postponed_bug[0]}
#
#     return  statistics_bug

