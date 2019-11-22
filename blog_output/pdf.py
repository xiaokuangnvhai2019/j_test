import pdfkit

url='https://www.cnblogs.com/xiaokuangnvhai/p/11676068.html'
confg=pdfkit.configuration(wkhtmltopdf=r'C:\zwj\besttest\wkhtmltox\bin\wkhtmltopdf.exe')

pdfkit.from_url(url,'aa.pdf',configuration=confg) #URL转换PDF

pdfkit.from_file('my.html','aa.pdf',configuration=confg) #文件转换PDF

html=''
pdfkit.from_string(html,'aa.pdf',configuration=confg) #字符串转换PDF
pdfkit.from_string(html,'aa.pdf',configuration=confg) #字符串转换PDF




