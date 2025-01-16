#!C:/Users/DELL/AppData/Local/Programs/Python/Python312/python
print("Content-Type:text/html")
print()
import cgi
f=cgi.FieldStorage()
t1=f.getvalue("t1")
t2=f.getvalue("t2")
t3=int(f.getvalue("t3"))
b1=f.getvalue("b1")
if(b1=="click"):
 news=t3+t3*.10
 f=open("D:\\emp.txt","a")
 f.write(t1)
 f.write(t2)
 f.write(str(t3))
 f.write(str(news))
 f.close()
 print("S")