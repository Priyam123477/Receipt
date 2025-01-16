#!C:/Users/DELL/AppData/Local/Programs/Python/Python312/python
print("Content-Type:text/html")
print()
import cgi
import traceback
from pymongo import MongoClient
import pymongo
f=cgi.FieldStorage()
t1=f.getvalue("t1")
t2=f.getvalue("t2")
t3=f.getvalue("t3")
t4=f.getvalue("t4")
t5=f.getvalue("t5")
s=f.getvalue("s")
t6=f.getvalue("t6")
t7=f.getvalue("t7")
t8=f.getvalue("t8")
t9=f.getvalue("t9")
b1=f.getvalue("b1")
try:
 if(b1=="Save"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['receipt']
  collection=db['reciept1']
  f=0
  for x in collection.find({}):
   if(x['sno']==t2):
    f=1
    break
  if(f==1):
   print("<script>alert('alreday exist')</script>")
   print("<script>window.open('reciept1.html','_self')</script>")
  else:
   insert1={'date1':t1,'sno':t2,'name':t3,'rupees':t4,'rswords':t5,'by':s,'drawn on':t6,'date2':t7,'onaccount':t8,'digitalsign':t9}
   collection.insert_one(insert1)
   print("<script>alert('Record Saved...')</script>")
   print("<script>window.open('reciept1.html','_self')</script>")
 if(b1=="AllSearch"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['receipt']
  collection=db['reciept1']
  print("<body><table border=2 cellpadding=18 ><tr bgcolor=lighblue><th>Date1</th><th>Serial No</th><th>Name</th><th>Rupees</th><th>Rupees in words</th><th>By</th><th>Drawn on</th><th>Date2</th><th>OnAccount of</th><th>Digitally Sign</th></tr>")
  for x in collection.find({}):
    print("<tr><th>",x['date1'],"</th>")
    print("<th>",x['sno'],"</th>")
    print("<th>",x['name'],"</th>")
    print("<th>",x['rupees'],"</th>")
    print("<th>",x['rswords'],"</th>")
    print("<th>",x['by'],"</th>")
    print("<th>",x['drawn on'],"</th>")
    print("<th>",x['date2'],"</th>")
    print("<th>",x['onaccount'],"</th>")
    print("<th>",x['digitalsign'],"</th></tr>")
  print("</table></body>")
except Exception:
   traceback.print_exc()

