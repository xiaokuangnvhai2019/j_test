import os

#二维数组变一维数组
def spread(arg):
    ret=[]
    for i in arg:
        if isinstance(i,tuple):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

#读文件
def read_file(file):
    f_html=open(file,encoding='utf-8')
    content=f_html.read()
    f_html.close()
    return  content


#list转换字典['xx',2,"yy",3]，转换 {'xx': 2, 'yy': 3}
def list_dic(list):
    if list:
        dic={}
        for index in range(0,len(list),2):
            dic[list[index]]=list[index+1]
    else:
        return  False
    return  dic

#清空文件
def clear(path):

    f = open(path, "a+", encoding="utf-8")  # 擦除写模式
    f.seek(0)
    f.truncate()  # 文件清空
    f.close()  # 关闭文件

#查找文件夹下带唯一标识的文件
def file_list(path,t_time):
    filename_list=[]
    all_file_list=os.listdir(path)
    for name in all_file_list:
        if t_time in name:
            filename_list.append(name)
        else:
            pass

    return filename_list





