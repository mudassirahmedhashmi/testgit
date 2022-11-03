from django.shortcuts import redirect
from django.http import HttpResponse
import mysql.connector as mysql
def home(req):
  return HttpResponse("""<h2>Welcome Home.....</h2><hr>
		<a href="/login">Login</a>
		<a href="/reg">Registration</a>
		<a href="/update"></a>
		

""")
def registration(req):
  return HttpResponse("""
            <div>
		<a href="/">Back</a>
	    </div>
	     <form action="/insertTask">
		<table align="center" border="2">
		  <tr>
		     <td>Name:</td>
		     <td>
	      		<input type="text" name="name">
		     </td>
		  </tr>
		  <tr>
		     <td>Father name:</td>
		     <td>
	      		<input type="text" name="fname">
		     </td>
		  </tr>
		  <tr>
		     <td>Email:</td>
		     <td>
	      		<input type="text" name="email">
		     </td>
		  </tr>
		  <tr>
		     <td>Password:</td>
		     <td>
	      		<input type="password" name="pass">
		     </td>
		  </tr>
		  <tr>
		     <td>Confirm Password:</td>
		     <td>
	      		<input type="password" name="cpass">
		     </td>
		  </tr>
		  <tr>
		     <td>Mobile:</td>
		     <td>
	      		<input type="text" name="mob">
		     </td>
		  </tr>
                  <tr>
		     
		     <td>
	      		<input type="submit" value="Register">
		     </td>
		 
		  </tr>
		   
		</table>
	    </form>
""")
def insertTask(req):
     name=req.GET.get("name")
     fname=req.GET.get("fname")
     email=req.GET.get("email")
     password=req.GET.get("pass")
     cpass=req.GET.get("cpass")
     mobile=req.GET.get("mob")

     con=mysql.connect(host="localhost",user="root",password="root",charset='utf8',database="django5")
     
     cr=con.cursor()
     sql="insert into reg (name,fname,email,password,mobile) values('{0}','{1}','{2}','{3}','{4}')".format(name,fname,email,password,mobile)
     cr.execute(sql)
     con.commit()     
  
     return redirect("/login")
  
def login(req):
  return HttpResponse("""
            <div>
		<a href="/">Back</a>
	    </div>
	     <form action="/loginTask">
		<table align="center" border="2">
		  
		  <tr>
		     <td>User:</td>
		     <td>
	      		<input type="text" name="email">
		     </td>
		  </tr>
		  <tr>
		     <td>Password:</td>
		     <td>
	      		<input type="password" name="pass">
		     </td>
		  </tr>
		   <tr>
		     
		     <td colspan="2">
	      		<input type="submit" value="Login">
		     </td>
		 
		  </tr>
		  <tr>
		     
		     <td colspan="2">
	      		<a href="/reg">New user....</a>
		     </td>
		 
		  </tr>
		   
		</table>
	    </form>
""")
def update(req):
  
  return HttpResponse("work on progress.....")
def search(req):
  con=mysql.connect(host="localhost",user="root",password="root",charset='utf8',database="django5")
  cr=con.cursor()
  sql="select * from student"
  cr.execute(sql)
  rec=cr.fetchall()
  return HttpResponse("<h3>"+str(rec)+"</h3>")

def loginTask(req):
  email=req.GET.get("email")
  password=req.GET.get("pass")
  con=mysql.connect(host="localhost",user="root",password="root",charset='utf8',database="django5")
  cr=con.cursor()
  sql="select * from reg where email='{0}' and password='{1}' ".format(email,password);  
  cr.execute(sql)
  rec=cr.fetchall()
  if(rec==[]):
     return redirect("/login") 
  else:
     global email1
     global name1
     global rec1

     email1=email
     rec1=rec
     for x in rec:
            name1=x[1]
     return redirect("/db")
     #return HttpResponse("Welcom "+name1)

def db(req):
  return HttpResponse(""" 

             Welcome in DB """+name1+"""<hr>
<br><a href='/login'>LogOut</a><br>
    <a href=''>Profile</a><br>

""")
  