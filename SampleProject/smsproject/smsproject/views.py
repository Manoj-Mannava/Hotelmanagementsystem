from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
import mysql.connector 
from django.core.files.storage import FileSystemStorage
import os


def convertToBinaryData(fileName):
 with open(fileName,'rb') as file:
  binaryData = file.read()
 return binaryData
def demofunction(request):
 return HttpResponse("MY NAME")
def homefunction(request):
 return render(request,"index3.html")
def aboutfunction(request):
 return render(request,"about.html")
def loginfunction(request):
 return render(request,"login.html")
def contactfunction(request):
 return render(request,"contact.html")
def userSignup(request):
 if request.method=="POST":
  username = request.POST.get('name')
  email=request.POST.get('email')
  password=request.POST.get('password12')
  mydb = mysql.connector.connect(
      user='root', password='ushoulddiehard', host='127.0.0.1', database='user'
  )
  mycursor = mydb.cursor()
  mycursor.execute("select * from signup where email='%s'" % (email))
  ulist = mycursor.fetchall()
  if ulist.__len__() >= 1:
   return HttpResponse("user already exists")
  mycursor1 = mydb.cursor()
  mycursor1.execute("INSERT INTO signup  VALUES(null,%s,%s,%s)", (username,email,password))
  mycursor2 = mydb.cursor()
  mycursor2.execute("select * from signup where email='%s'" % (email))
  ulist2=mycursor2.fetchall()
  id=str(ulist2[0][0])
  mycursor3 = mydb.cursor()
  mycursor3.execute("CREATE TABLE user1_"+id+"(roomno int UNIQUE)")
  mycursor4 = mydb.cursor()
  mycursor4.execute("CREATE TABLE user2_"+id+"(id int AUTO_INCREMENT key,hotelName varchar(100),roomno int,hotel varchar(100))")
  mydb.commit()
  return render(request,"userSignup.html")
 return render(request,"userSignup.html")

def userLogin(request):
 if request.method=="POST":
  email=request.POST.get('email1')
  password=request.POST.get('password1')
  mydb = mysql.connector.connect(
      user='root', password='ushoulddiehard', host='127.0.0.1', database='user'
  )
  mycursor = mydb.cursor()
  mycursor.execute("select * from signup where email='%s'" % (email))
  ulist = mycursor.fetchall()
  if ulist.__len__() == 0:
   return HttpResponse("your user email doesnot exists")
  mycursor1 = mydb.cursor()
  mycursor1.execute("SELECT * FROM signup WHERE email=%s and password=%s ", (email, password))
  login1 = mycursor1.fetchall()
  if login1.__len__() >= 1:
   global id1
   id1=str(login1[0][0])
   global name1
   name1=login1[0][1]
   return redirect('user0')
  else:
      return HttpResponse("your entered password in correct")
 return HttpResponse("MANNAVA KAMAL")

def user0(request):
 mydb = mysql.connector.connect(
  user='root', password='ushoulddiehard', host='127.0.0.1', database='Admin'
 )
 mycursor = mydb.cursor()
 mycursor.execute("SELECT id,name FROM signup")
 adminDetails = mycursor.fetchall()
 mydb.commit()
 print(adminDetails)
 return render(request,'user0.html',{
     "name":name1,
     "adminDetails":adminDetails,
 })
def hotelSelect(request):
 if request.method == "GET":
  global data
  data = request.GET['data']
  print(data)
  return HttpResponse("yes Iam there")
 return HttpResponse("yes Iam there")
def user1(request):
 mydb = mysql.connector.connect(
  user='root', password='ushoulddiehard', host='127.0.0.1', database='Admin'
 )
 mycursor = mydb.cursor()
 mycursor.execute("SELECT * FROM user1_"+data)
 roomdetails = mycursor.fetchall()
 mydb.commit()
 return render(request,"user1.html",{
     'name':name1,
  'roomdetails': roomdetails,
  'booked':0
 })
def bookedrooms(request):
    if request.method == "GET":
        data = request.GET['data']
        roomType = request.GET['roomType']
        data1 = int(data)
        print(data1)
        print(roomType)
        mydb = mysql.connector.connect(
            user='root', password='ushoulddiehard', host='127.0.0.1', database='user'
        )
        # Another quary
        mycursor2 = mydb.cursor()
        mycursor2.execute("TRUNCATE TABLE user1_"+id1)
        # Another quary
        mycursor3 = mydb.cursor()
        mycursor3.execute("INSERT INTO user1_"+id1+" VALUES(%d)" % (data1))
        mydb.commit()
    return HttpResponse("kaalmla")
def bookingProcess(request):
 mydb = mysql.connector.connect(
 user='root', password='ushoulddiehard', host='127.0.0.1', database='user'
    )
 mydb1 = mysql.connector.connect(
 user='root', password='ushoulddiehard', host='127.0.0.1', database='Admin'
    )
 mycursor = mydb.cursor()
 mycursor.execute("select * from user1_"+id1)
 booking = mycursor.fetchall()
 print(booking)
 print(booking[0][0])
 adminroomNo = booking[0][0]
 mycursor1 = mydb1.cursor()
 mycursor1.execute("select * from user1_"+data+" where roomNo=(%d)" % (adminroomNo))
 adminRoom=mycursor1.fetchall()
 print(adminRoom[0][0])
 print(adminRoom[0][1])
 print(adminRoom[0][2])
 print(adminRoom[0][4])
 return render(request,"booking process.html",{
  'roomnoimg': adminRoom[0][4],
  'roomno':adminRoom[0][0],
  'roomtype':adminRoom[0][1],
 })
def roomConformed(request):
    mydb = mysql.connector.connect(
        user='root', password='ushoulddiehard', host='127.0.0.1', database='user'
    )
    mycursor = mydb.cursor()
    mycursor.execute("select * from user1_" + id1)
    booking = mycursor.fetchall()
    mydb.commit()
    print(booking)
    print(booking[0][0])
    adminroomNo = booking[0][0]
    mydb1 = mysql.connector.connect(
        user='root', password='ushoulddiehard', host='127.0.0.1', database='Admin'
    )
    mycursor1 = mydb1.cursor()
    mycursor1.execute("select * from user1_" + data + " where roomNo=(%d)" % (adminroomNo))
    adminRoom = mycursor1.fetchall()
    mydb1.commit()
    mydb2 = mysql.connector.connect(
        user='root', password='ushoulddiehard', host='127.0.0.1', database='Admin'
    )
    mycursor2 = mydb2.cursor()
    mycursor2.execute("UPDATE user1_"+data+" SET booked =%2d WHERE roomno=%2d" % (1,adminroomNo))
    mydb2.commit()

    print(adminRoom[0][0])
    print(adminRoom[0][1])
    print(adminRoom[0][2])
    print(adminRoom[0][4])
    return render(request, "roomConformed.html", {
        'roomnoimg': adminRoom[0][4],
        'roomno': adminRoom[0][0],
        'roomtype': adminRoom[0][1],
    })
def user2(request):
 mydb = mysql.connector.connect(
  user='root', password='ushoulddiehard', host='127.0.0.1', database='sampleproject'
 )
 mycursor = mydb.cursor()
 mycursor.execute("SELECT * FROM roomsBookedTillDate ")
 roomdetails = mycursor.fetchall()
 return render(request, "user2.html",{
  'roomdetailslength':range(0,roomdetails.__len__()),
  'roomdetails': roomdetails,
 })
def roomEntry(request):
  roomNo = request.POST['roomNo']
  roomNo1 = int(roomNo)
  roomType = request.POST['roomType']
  img1 = request.FILES['img']
  #print(img1.name) image name
  #print(img1)
  mydb = mysql.connector.connect(
   user='root', password='ushoulddiehard', host='127.0.0.1', database='Admin'
  )
  mycursor = mydb.cursor()
  mycursor.execute("SELECT roomno FROM user1_"+id+" where roomno=%2d " % (roomNo1))
  roomNo2 = mycursor.fetchall()
  res_len = roomNo2.__len__()
  if (res_len == 1):
   return HttpResponse("you entered roomNo already exists")
  fs = FileSystemStorage()
  fs.save(img1.name, img1)
  path = os.path.join(r"C:\Users\DELL\OneDrive\Desktop\project\SampleProject\SampleProject\smsproject\media", img1.name)
  str = convertToBinaryData(path)
  sqlr="user1_"+id+"img"+roomNo
  mycursor1 = mydb.cursor()
  mycursor1.execute("INSERT INTO user1_"+id+" VALUES (%s,%s,%s,%s,%s)",(roomNo,roomType,0,str,sqlr))
  mydb.commit()
  os.remove(path)
  return redirect('Admin2')
def adminSignup(request):
 if request.method=="POST":
  username = request.POST.get('name')
  email=request.POST.get('email')
  password=request.POST.get('password12')
  mydb = mysql.connector.connect(
      user='root', password='ushoulddiehard', host='127.0.0.1', database='Admin'
  )
  mycursor = mydb.cursor()
  mycursor.execute("select * from signup where email='%s'" % (email))
  ulist = mycursor.fetchall()
  if ulist.__len__() >= 1:
   return HttpResponse("Admin already exists")
  mycursor1 = mydb.cursor()
  mycursor1.execute("INSERT INTO signup  VALUES(null,%s,%s,%s)", (username,email,password))
  mycursor2 = mydb.cursor()
  mycursor2.execute("select * from signup where email='%s'" % (email))
  ulist2=mycursor2.fetchall()
  id=str(ulist2[0][0])
  mycursor3 = mydb.cursor()
  mycursor3.execute("CREATE TABLE user1_"+id+"(roomno int UNIQUE,roomtype varchar(100),booked int,image mediumblob,imgstr varchar(100))")
  mydb.commit()
  return render(request,"adminSignup.html")
 return render(request,"adminSignup.html")
def adminLogin(request):
 if request.method=="POST":
  email=request.POST.get('email1')
  password=request.POST.get('password1')
  mydb = mysql.connector.connect(
      user='root', password='ushoulddiehard', host='127.0.0.1', database='Admin'
  )
  mycursor = mydb.cursor()
  mycursor.execute("select * from signup where email='%s'" % (email))
  ulist = mycursor.fetchall()
  if ulist.__len__() == 0:
   return HttpResponse("your admin email doesnot exists")
  mycursor1 = mydb.cursor()
  mycursor1.execute("SELECT * FROM signup WHERE email=%s and password=%s ", (email, password))
  login1 = mycursor1.fetchall()
  if login1.__len__() >= 1:
   print(login1)
   global id
   id=str(login1[0][0])
   global name
   name=login1[0][1]
   return render(request,"Admin1.html",{
        'name': name,
    })
  else:
      return HttpResponse("your entered password in correct")
 return HttpResponse("MANNAVA KAMAL")
def Admin1(request):
 return render(request, "Admin1.html",{
        'name': name,
    })
def Admin2(request):
 mydb = mysql.connector.connect(
  user='root', password='ushoulddiehard', host='127.0.0.1', database='Admin'
 )
 mycursor = mydb.cursor()
 mycursor.execute("SELECT * FROM user1_"+id )
 roomdetails = mycursor.fetchall()
 for x1 in roomdetails:
  mycursor.execute("SELECT * FROM user1_"+id+" where roomno = {0}".format(x1[0]))
  c3 = mycursor.fetchone()[3]
  c4 = "user1_"+id+"img{0}.png".format(x1[0])
  path = os.path.join(r"C:\Users\DELL\OneDrive\Desktop\project\SampleProject\SampleProject\smsproject", c4)
  with open(path, "wb") as file:
   file.write(c3)
   file.close()
 return render(request, "Admin2.html", {
  'roomdetailslength': range(0, roomdetails.__len__()),
  'roomdetails': roomdetails,
 })
def deleteAdminRooms(request):
 data = request.GET['data']
 roomType = request.GET['roomType']
 data1 = int(data)
 c4 = "user1_"+id+"img{0}.png".format(data1)
 path = os.path.join(r"C:\Users\DELL\OneDrive\Desktop\project\SampleProject\SampleProject\smsproject", c4)
 os.remove(path)
 mydb = mysql.connector.connect(
  user='root', password='ushoulddiehard', host='127.0.0.1', database='Admin'
 )
 mycursor = mydb.cursor()
 mycursor.execute("DELETE FROM user1_"+id+" WHERE roomno=%2d  " % (data1))
 mydb.commit()
 var1 = "room"+data+"deleated suceessfully just reload the page"
 return HttpResponse({var1})
def Admin3(request):
 mydb = mysql.connector.connect(
  user='root', password='ushoulddiehard', host='127.0.0.1', database='Admin'
 )
 mycursor = mydb.cursor()
 mycursor.execute("SELECT * FROM user1_"+id+" where booked=1")
 roomdetails = mycursor.fetchall()
 return render(request, "Admin3.html", {
  'roomdetails': roomdetails,
 })

def index(request):
    return render(request,"index2.html")