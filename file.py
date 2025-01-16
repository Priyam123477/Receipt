#!C:/Users/DELL/AppData/Local/Programs/Python/Python312/python
print("Content-Type:text/html")
print()
import cgi
f=cgi.FieldStorage()
t1=f.getvalue("t1")
b1=f.getvalue("b1")
f=open("D:\\mytest.txt","a")
f.write(t1)
f.close()