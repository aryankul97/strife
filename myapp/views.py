from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.mail import EmailMessage
from myapp.models import *
from django.contrib import messages
import datetime
import uuid
import random
from random import shuffle
from collections import OrderedDict


now=datetime.datetime.now()
@csrf_exempt
def bout(request):
	"""a=AddComp.objects.all()
	b=NewAdmin.objects.all()
	c=CanData.objects.all()
	d=CompQuiz.objects.all()
	f=CanMarks.objects.all()
	a.delete()
	b.delete()
	c.delete()
	d.delete()
	f.delete()
	ob=NewAdmin.objects.filter(Admin_Name="Sonali").update(Institution_Name="HITM")
	ob=NewAdmin.objects.all()
	ob.delete()
	email=EmailMessage('Strife','Hello',to=['sonalikul1999@gmail.com'])
	email.send()"""
	ob=AddComp.objects.all()
	filedata=File.objects.all()
	b1="Hello"
	b2=" "
	b3=" "
	b4=" "
	b5=" "
	for elt in filedata:
		if elt.FName=="q1":
			b1=elt.FData
			break
	for elt in filedata:
		if elt.FName=="q4":
			b2=elt.FData
			break
	for elt in filedata:
		if elt.FName=="q5":
			b3=elt.FData
			break
	for elt in filedata:
		if elt.FName=="q6":
			b4=elt.FData
			break
	for elt in filedata:
		if elt.FName=="q7":
			b5=elt.FData
			break
	compname=b1
	Status="Y"
	for elt in ob:
		if elt.Status=="Y":
			comp=b2+elt.Comp_Name+b3+elt.Comp_Name+b4
			compname=compname+comp
	compname=compname+b5
	context={'compname':compname}
	return render(request,'bout.html',context)
def startquiz(request):
	return render(request,'startquiz.html',{'alert':"Start Quiz Here!"})
def quiz(request):
	return render(request,'quiz.html',{})
def adminlogin(request):
	return render(request,'admin.html',{})
def newadmin(request):
	return render(request,'newadmin.html',{})
def adminprofile(request):
	return render(request,'adminprofile.html',{})
def forgot(request):
	return render(request,'forgotpassword.html',{})
@csrf_exempt
def saveadmin(request):
	if request.method=="POST":
		i=request.POST.get('name')
		n=request.POST.get('admin')
		a=request.POST.get('adminpost')
		m=request.POST.get('mobile')
		e=request.POST.get('email')
		p=str(uuid.uuid5(uuid.NAMESPACE_DNS, i+n+a+m+e))
		filedata=File.objects.all()
		b1="Hello"
		b2=" "
		for elt in filedata:
			if elt.FName=="alert1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="alert2":
				b2=elt.FData
				break
		ob=NewAdmin.objects.all()
		d=0
		for elt in ob:
			if m==elt.Mobile or e==elt.Email:
				d=1
				alert=b1+"User Already Exists"+b2
				return render(request,'newadmin.html',{'alert':alert})
				break
		if d==0:
			#obj=NewAdmin(Paid="N",Institution_Name=i,Admin_Name=n,Admin_Post=a,Mobile=m,Email=e,Password=p)
			obj=NewAdmin(Paid="Y",Institution_Name=i,Admin_Name=n,Admin_Post=a,Mobile=m,Email=e,Password=p)
			maill="Hi "+n+"\nYour Account has been successfully created,\nyour account password is "+p+"\n\nPay Rs.1000/- for One Year Subscription of STRIFE.\n\nThanks & Regards\nTeam Strife"
			emaill=EmailMessage('Strife-Admin Registration Successful',maill,to=[e])
			emaill.send()
			maill="Institute Name- "+i+"\nAdmin Name- "+n+"\nAdmin Designation- "+a+"\nMobile- "+m+"\nEmail- "+e+"\n\nThanks & Regards\nTeam Strife"
			emaill=EmailMessage('Admin Registration',maill,to=["strifeapp99@gmail.com"])
			emaill.send()
			obj.save()
			request.session['AdminEmail'] = request.POST['email']
			request.session['AdminPass'] = p
			#return render(request,'userres.html',{})
			alert=b1+"Account Created Successfully, We have sent your password to your email which you can further change."+b2
			#print(alert)
			return render(request,'admin.html',{'alert':alert})
@csrf_exempt
def savecomp(request):
	if request.method=="POST":
		c=request.POST.get('compname')
		ca=request.POST.get('category')
		about=request.POST.get('about')
		mm=request.POST.get('mm')
		noques=request.POST.get('noques')
		marksques=request.POST.get('marksques')
		time=request.POST.get('time')
		time=int(time)
		mm=int(mm)
		noques=int(noques)
		marksques=int(marksques)
		email = request.session['Email']
		obj=NewAdmin.objects.all()
		passw=request.POST.get('pass')
		d=0
		p=0
		mobile=" "
		for elt in obj:
			if email==elt.Email and passw==elt.Password:
				p=1
				break
		for elt in obj:
			if email==elt.Email:
				mobile=elt.Mobile
				break
		ob=AddComp.objects.all()
		d=0
		for elt in ob:
			if c==elt.Comp_Name:
				d=1
				return render(request,'compexist.html',{})
				break
		compid=c+mobile
		if d==0 and p==1:
			obj=AddComp(Time=time,Comp_ID=compid,Admin_ID=mobile,Comp_Name=c,Cate_Name=ca,About_Comp=about,Number_Ques=noques,MaxMarks=mm,MarksPerQues=marksques,Status="Y")
			obj.save()
			return render(request,'compres.html',{})
		else:
			return render(request,'compass.html',{})
@csrf_exempt
def checklogin(request):
    d=0
    i=request.POST.get('id')
    p=request.POST.get('pass')
    obj=NewAdmin.objects.all()
    s="Y"
    ps=0
    context={}
    filedata=File.objects.all()
    al1="Hello"
    al2=" "
    for elt in filedata:
    	if elt.FName=="alert1":
    		al1=elt.FData
    		break
    for elt in filedata:
    	if elt.FName=="alert2":
    		al2=elt.FData
    		break
    for elt in obj:
    	if i==elt.Email and p==elt.Password:
    		request.session['Email'] = request.POST['id']
    		d=1
    		context={'admin':elt.Admin_Name}
    		if s==elt.Paid:
    			request.session['AdminName'] = elt.Admin_Name
    			context={'admin':elt.Admin_Name,
    					'post':elt.Admin_Post,
    					'name':elt.Institution_Name,
    					'email':elt.Email,
    					'mobile':elt.Mobile,
    					'unique':elt.Mobile}
    			print(context)
    			b=list(context.items())
    			shuffle(b)
    			context=OrderedDict(b)
    			print(context)
    			ps=1
    			break
    if ps==0 and d==1:
    	request.session['AdminEmail'] = request.POST['id']
    	request.session['AdminPass'] = request.POST['pass']
    	return render(request,"userres.html",context)
    if d==0:
    	alert=al1+"Incorrect Email or Password"+al2
    	return render(request,'admin.html',{'alert':alert})
    if d==1 and ps==1:
    	return render(request,'adminprofile.html',context)
@csrf_exempt
def forgotpassword(request):
	i=request.POST.get('id')
	b1=" "
	b2=" "
	obj=NewAdmin.objects.all()
	mail="Hello,\nYour Password is"
	for elt in obj:
		if i==elt.Email:
			mail="Hello "+elt.Admin_Name+",\nYour Password is "+elt.Password+"\nThanks & Regards\n"+"Team Strife"
			email=EmailMessage('Strife-Forgot Password',mail,to=[elt.Email])
			email.send()
			filedata=File.objects.all()
			b1=" "
			b2=" "
			for elt in filedata:
				if elt.FName=="alert1":
					b1=elt.FData
					break
			for elt in filedata:
				if elt.FName=="alert2":
					b2=elt.FData
					break
			alert=b1+"We have sent a mail. Check your email."+b2
			context={'alert':alert}
			return render(request,'admin.html',context)
			break
		else:
			alert=b1+"No such email found."+b2
			context={'alert':alert}
			return render(request,'forgotpassword.html',context)
@csrf_exempt
def backlogin(request):
	d=0
	i = request.session['Email']
	obj=NewAdmin.objects.all()
	for elt in obj:
		if i==elt.Email:
			context={'admin':elt.Admin_Name,
					'post':elt.Admin_Post,
					'name':elt.Institution_Name,
					'email':elt.Email,
					'mobile':elt.Mobile,
					'unique':elt.Mobile}
			d=1
			break
	if d==0:
		return render(request,"nouser.html",{})
	else:
		return render(request,'adminprofile.html',context)
@csrf_exempt
def compdata(request):
	text=" "
	d=0
	ob=AddComp.objects.all()
	filedata=File.objects.all()
	b1=" "
	b2=" "
	b3=" "
	b4=" "
	for elt in filedata:
		if elt.FName=="c1":
			b1=elt.FData
			break
	for elt in filedata:
		if elt.FName=="c2":
			b2=elt.FData
			break
	for elt in filedata:
		if elt.FName=="c3":
			b3=elt.FData
			break
	for elt in filedata:
		if elt.FName=="c4":
			b4=elt.FData
			break
	blog=""
	Status="Y"
	obj=NewAdmin.objects.all()
	mob = request.session['Email']
	for elt in obj:
		if mob==elt.Email:
			mob=elt.Mobile
			request.session["Admin_ID"] = mob
	for elt in ob:
		if mob==elt.Admin_ID and elt.Status==Status:
			comp=b1+elt.Comp_ID+b2+elt.Comp_Name+b3+elt.Cate_Name+b4
			blog=blog+comp+"\n"
	context={'comp':blog}
	return render(request,'comp.html',context)
@csrf_exempt
def deactivecomp(request):
	text=" "
	d=0
	ob=AddComp.objects.all()
	filedata=File.objects.all()
	b1=" "
	b2=" "
	b3=" "
	b4=" "
	for elt in filedata:
		if elt.FName=="s1":
			b1=elt.FData
			break
	for elt in filedata:
		if elt.FName=="s2":
			b2=elt.FData
			break
	for elt in filedata:
		if elt.FName=="s3":
			b3=elt.FData
			break
	for elt in filedata:
		if elt.FName=="s4":
			b4=elt.FData
			break
	blog=""
	Status="N"
	obj=NewAdmin.objects.all()
	mob = request.session['Email']
	for elt in obj:
		if mob==elt.Email:
			mob=elt.Mobile
			request.session["Admin_ID"] = mob
	for elt in ob:
		if mob==elt.Admin_ID and elt.Status==Status:
			comp=b1+elt.Comp_ID+b2+elt.Comp_Name+b3+elt.Cate_Name+b4
			blog=blog+comp+"\n"
	context={'comp':blog}
	return render(request,'deactivecomp.html',context)
@csrf_exempt
def compques(request):
	if request.method=="POST":
		filedata=File.objects.all()
		b1=" "
		b2=" "
		b3=" "
		b4=" "
		b5=" "
		b6=" "
		b7=" "
		for elt in filedata:
			if elt.FName=="w1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w2":
				b2=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w3":
				b3=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w4":
				b4=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w5":
				b5=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w6":
				b6=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w7":
				b7=elt.FData
				break
		da="<h1>Hello</h1>"
		request.session['CompID'] = request.POST.get('compid')
		a=request.POST.get('compid')
		obj=CompQuiz.objects.all()
		for elt in obj:
			if a==elt.Comp_ID:
				print(elt.Ques_No)
				ques=b1+elt.Ques+b2+elt.A+b3+elt.B+b4+elt.C+b5+elt.D+b6+elt.Answer+b7
				da=da+ques+"\n"
		context={}
		obj=AddComp.objects.all()
		for elt in obj:
			if a==elt.Comp_ID:
				context={'ques':da,
						'name':elt.Comp_Name,
						'cate':elt.Cate_Name,
						'about':elt.About_Comp,
						'quesno':elt.Number_Ques,
						'marks':elt.MarksPerQues,
						'maxmarks':elt.MaxMarks}
		return render(request,'compques.html',context)
#Adding Questions
@csrf_exempt
def addques(request):
	if request.method=="POST":
		cid = request.session['CompID']
		aid = request.session['Admin_ID']
		q=request.POST.get('ques')
		a=request.POST.get('A')
		b=request.POST.get('B')
		c=request.POST.get('C')
		d=request.POST.get('D')
		ans=request.POST.get('ans')
		x=1
		filedata=File.objects.all()
		b1=" "
		b2=" "
		obj=AddComp.objects.filter(Comp_ID=cid)
		for elt in obj:
			no=elt.Number_Ques
			no=int(no)
			break
		cidd=cid+str(x)
		while CompQuiz.objects.filter(Ques_No=cidd).exists():
			x=x+1
			cidd=cid+str(x)
		x=int(x)
		filedata=File.objects.all()
		a1=" "
		a2=" "
		for elt in filedata:
			if elt.FName=="alert1":
				a1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="alert2":
				a2=elt.FData
				break
		if x<=no:
			obj=CompQuiz(Admin_ID=aid,Comp_ID=cid,Ques_No=cidd,Ques=q,A=a,B=b,C=c,D=d,Answer=ans)
			obj.save()
			alert=a1+"Added Successfully!"+a2
		else:
			alert=a1+"You have exceeded the maximum Limit!"+a2
		filedata=File.objects.all()
		b1=" "
		b2=" "
		b3=" "
		b4=" "
		b5=" "
		b6=" "
		b7=" "
		for elt in filedata:
			if elt.FName=="w1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w2":
				b2=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w3":
				b3=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w4":
				b4=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w5":
				b5=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w6":
				b6=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w7":
				b7=elt.FData
				break
		da="<h1>Hello</h1>"
		a = request.session['CompID']
		obj=CompQuiz.objects.all()
		for elt in obj:
			if a==elt.Comp_ID:
				ques=b1+elt.Ques+b2+elt.A+b3+elt.B+b4+elt.C+b5+elt.D+b6+elt.Answer+b7
				da=da+ques+"\n"
		obj=AddComp.objects.all()
		context={}
		for elt in obj:
			if a==elt.Comp_ID:
				name=elt.Comp_Name
				context={'ques':da,
						'name':elt.Comp_Name,
						'cate':elt.Cate_Name,
						'about':elt.About_Comp,
						'quesno':elt.Number_Ques,
						'marks':elt.MarksPerQues,
						'maxmarks':elt.MaxMarks,
						'alert':alert}
		return render(request,'compques.html',context)
#Generate CSV Of Questions
@csrf_exempt
def quesPDF(request):
	cid = request.session['CompID']
	aid = request.session['Admin_ID']
	name=" "
	obj=AddComp.objects.filter(Comp_ID=cid)
	for elt in obj:
		name=elt.Comp_Name
	response = HttpResponse()
	response['Content-Disposition'] = 'attachment;filename='+name+'.csv'
	writer = csv.writer(response)
	writer.writerow(["Ques ID", "Question", "Option A", "Option B", "Option C", "Option D", "Answer"])
	obj1=CompQuiz.objects.filter(Comp_ID=cid)
	for elt in obj1:
		writer.writerow([elt.Ques_No, elt.Ques, elt.A, elt.B, elt.C, elt.D, elt.Answer])
	return response
@csrf_exempt
def ques(request):
		filedata=File.objects.all()
		b1=" "
		b2=" "
		b3=" "
		b4=" "
		b5=" "
		b6=" "
		b7=" "
		for elt in filedata:
			if elt.FName=="w1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w2":
				b2=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w3":
				b3=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w4":
				b4=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w5":
				b5=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w6":
				b6=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w7":
				b7=elt.FData
				break
		da="<h1>Hello</h1>"
		a = request.session['CompID']
		obj=CompQuiz.objects.all()
		for elt in obj:
			if a==elt.Comp_ID:
				ques=b1+elt.Ques+b2+elt.A+b3+elt.B+b4+elt.C+b5+elt.D+b6+elt.Answer+b7
				da=da+ques+"\n"
		obj=AddComp.objects.all()
		context={}
		for elt in obj:
			if a==elt.Comp_ID:
				name=elt.Comp_Name
				context={'ques':da,
						'name':elt.Comp_Name,
						'cate':elt.Cate_Name,
						'about':elt.About_Comp,
						'quesno':elt.Number_Ques,
						'marks':elt.MarksPerQues,
						'maxmarks':elt.MaxMarks}
		return render(request,'compques.html',context)
@csrf_exempt
def deaccomp(request):
		compid = request.session['CompID']
		print(compid)
		ob=AddComp.objects.filter(Comp_ID=compid).update(Status="N")
		return render(request,'deaccomp.html',{})
@csrf_exempt
def activecomp(request):
		if request.method=="POST":
			a=request.POST.get('compid')
			ob=AddComp.objects.filter(Comp_ID=a).update(Status="Y")
			return render(request,'activecomp.html',{})
@csrf_exempt
def saveCan(request):
	if request.method=="POST":
		r=request.POST.get('roll')
		n=request.POST.get('name')
		e=request.POST.get('email')
		c=request.POST.get('compname')
		cour=request.POST.get('course')
		b=request.POST.get('bra')
		i=request.POST.get('inst')
		d=0
		compid=" "
		adminid=" "
		obj=AddComp.objects.all()
		objj=NewAdmin.objects.all()
		for elt in obj:
			if c==elt.Comp_Name:
				compid=elt.Comp_ID
				adminid=elt.Admin_ID
				break
		adminmail="strifeapp99@gmail.com"
		for elt in objj:
			if adminid==elt.Mobile:
				adminmail=elt.Email
				break
		filedata=File.objects.all()
		al1=" "
		al2=" "
		for elt in filedata:
			if elt.FName=="alert1":
				al1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="alert2":
				al2=elt.FData
				break
		ob=AddComp.objects.all()
		b1="Hello"
		b2=" "
		b3=" "
		b4=" "
		b5=" "
		for elt in filedata:
			if elt.FName=="q1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q4":
				b2=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q5":
				b3=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q6":
				b4=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q7":
				b5=elt.FData
				break
		compname=b1
		Status="Y"
		for elt in ob:
			if elt.Status=="Y":
				comp=b2+elt.Comp_Name+b3+elt.Comp_Name+b4
				compname=compname+comp
		compname=compname+b5
		ob=CanData.objects.all()
		for elt in ob:
			if r==elt.Can_ID and compid==elt.Comp_ID:
				d=1
				alert=al1+"Candidate Already Exists"+al2
				context={'compname':compname,
						'alert':alert}
				return render(request,'bout.html',context)
				break

		if d==0:
			loginid="strife"+r
			obj=CanData(Login_ID=loginid,Can_ID=r,Candidate_Name=n,Candidate_Email=e,Comp_ID=compid,Course=cour,Branch=b,Institution_Name=i)
			mail="Congrats "+n+",\n\nYou have successfully registered for "+c+",\n\nYour Login ID is "+loginid+"\nuse this login id to access your account and start quiz. And the password will be provided by the Competition Organizer.\n\nThanks & Regards\nTeam Strife"
			email=EmailMessage('Congratulations',mail,to=[e])
			maill="Name- "+n+"\nRoll Number- "+r+"\nEmail- "+e+"\nCompetition Name- "+c+"\nInstitute Name- "+i+"\nCourse- "+cour+"\nBranch- "+b+"\n\nThanks & Regards\nTeam Strife"
			emaill=EmailMessage('Candidate Registration',maill,to=[adminmail])
			emaill.send()
			email.send()
			obj.save()
			alert=al1+"Candidate Successfully Registered, We have sent you a mail with your Login Id."+al2
			context={'compname':compname,
					'alert':alert}
			return render(request,'bout.html',context)
@csrf_exempt
def checkcandidate(request):
	if request.method=="POST":
		d=0
		i=request.POST.get('id')
		p=request.POST.get('pass')
		filedata=File.objects.all()
		b1=" "
		b2=" "
		b3=" "
		b4=" "
		b5=" "
		b6=" "
		b7=" "
		b8=" "
		b9=" "
		b10=" "
		b11=" "
		b12=" "
		for elt in filedata:
			if elt.FName=="qu1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="qu2":
				b2=elt.FData
				break
		for elt in filedata:
			if elt.FName=="qu3":
				b3=elt.FData
				break
		for elt in filedata:
			if elt.FName=="qu4":
				b4=elt.FData
				break
		for elt in filedata:
			if elt.FName=="qu5":
				b5=elt.FData
				break
		for elt in filedata:
			if elt.FName=="qu6":
				b6=elt.FData
				break
		for elt in filedata:
			if elt.FName=="qu7":
				b7=elt.FData
				break
		for elt in filedata:
			if elt.FName=="qu8":
				b8=elt.FData
				break
		for elt in filedata:
			if elt.FName=="qu9":
				b9=elt.FData
				break
		for elt in filedata:
			if elt.FName=="qu10":
				b10=elt.FData
				break
		for elt in filedata:
			if elt.FName=="qu11":
				b11=elt.FData
				break
		for elt in filedata:
			if elt.FName=="qu12":
				b12=elt.FData
				break
		comp=" "
		ques=" "
		send=" "
		canid=" "
		context={}
		obj=CanData.objects.all()
		ob=AddComp.objects.filter(Status='Y')
		obb=CompQuiz.objects.all()
		ctime=0
		send=[]
		compid=" "
		for elt in obj:
			if i==elt.Login_ID and p==elt.Comp_ID:
				canid=elt.Can_ID
				compid=elt.Comp_ID
				for x in ob:
					if elt.Comp_ID==x.Comp_ID:
						request.session['Can_ID'] = elt.Can_ID
						request.session['Can_Comp_ID'] = elt.Comp_ID
						d=1
						comp=x.Comp_Name
						ctime=60000*x.Time
						obb=CompQuiz.objects.filter(Comp_ID=p)
						i=1

						for x in obb:
							i=str(i)
							ques=b1+"ques"+i+b2+x.Ques_No+b3+x.Ques+b4+"option"+i+b5+x.A+b6+"option"+i+b7+x.B+b8+"option"+i+b9+x.C+b10+"option"+i+b11+x.D+b12
							send.append(ques)
							"""print(context)
							b=list(context.items())
							shuffle(b)
							context=OrderedDict(b)
							print(context)"""
							i=int(i)
							i=i+1
						break
				shuffle(send)
				ques=" "
				for i in range(0,len(send)):
					ques=ques+send[i]
				context={'roll':elt.Can_ID,
					'name':elt.Candidate_Name,
					'email':elt.Candidate_Email,
					'comp':comp,
					'course':elt.Course,
					'branch':elt.Branch,
					'send':ques,
					'time':ctime}
				break
		obj=CanMarks.objects.all()
		for elt in obj:
			if canid==elt.Can_ID and compid==elt.Comp_ID:
				alert="You have already taken part"
				context={'alert':alert}
				return render(request,"startquiz.html",context)
		if d==0:
			alert="Incorrect Login ID or Competition ID"
			return render(request,"startquiz.html",{'alert':alert})
		else:
			return render(request,'quiz.html',context)
@csrf_exempt
def gnerateresult(request):
	if request.method=="POST":
		canid = request.session['Can_ID']
		compid = request.session['Can_Comp_ID']
		obj=CanData.objects.all()
		canname="Not Found"
		canemail=" "
		for elt in obj:
			if canid==elt.Can_ID:
				canname=elt.Candidate_Name
				canemail=elt.Candidate_Email
				break
		obj=CompQuiz.objects.filter(Comp_ID=compid)
		obj1=AddComp.objects.filter(Comp_ID=compid)
		q='ques'
		o='option'
		marks=0
		maxQ=5
		compname=" "
		marksperq=1
		orgname=" "
		for elt in obj1:
			maxQ=elt.Number_Ques
			compname=elt.Comp_Name
			marksperq=elt.MarksPerQues
			orgname=elt.Admin_ID
			break
		ad=NewAdmin.objects.filter(Mobile=orgname)
		for x in ad:
			orgname=x.Institution_Name
		for x in range(1,maxQ+1):
			qu=q+str(x)
			ob=o+str(x)
			for elt in obj:
				if request.POST.get(qu)==elt.Ques_No:
					if request.POST.get(ob)==elt.Answer:
						marks=marks+marksperq
		obj=CanMarks(Comp_ID=compid,Can_ID=canid,Marks=marks)
		percent=0.0
		context={}
		for elt in obj1:
			percent=(marks/elt.MaxMarks)*100
			context={'name':canname,
					'percent':percent,
					'marks':marks,
					'mm':elt.MaxMarks,
					'roll':canid}
		maill="Hello "+canname+"\nYou have scored "+str(percent)+"% in "+compname+", organized by "+orgname+"\n\nThanks & Regards\nTeam Strife"
		emaill=EmailMessage('Strife Result',maill,to=[canemail])
		emaill.send()
		obj.save()
		obj=AddComp.objects.filter(Comp_ID=compid)
		for elt in obj:
			adminid=elt.Admin_ID
			break
		"""if adminid=='7417358703':
			return render(request,'supercanmarks.html',context)
		else:
			return render(request,'canmarks.html',context)"""
		return render(request,'canmarks.html',context)
@csrf_exempt
def results(request):
		filedata=File.objects.all()
		b1=" "
		b2=" "
		b3=" "
		b4=" "
		b5=" "
		b6=" "
		b7=" "
		for elt in filedata:
			if elt.FName=="w1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w2":
				b2=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w3":
				b3=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w4":
				b4=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w5":
				b5=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w6":
				b6=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w7":
				b7=elt.FData
				break
		da="<h1>Hello</h1>"
		a = request.session['CompID']
		obj=CanMarks.objects.all()
		obj1=CanData.objects.all()
		for elt in obj:
			if a==elt.Comp_ID:
				for x in obj1:
					if elt.Can_ID==x.Can_ID and a==x.Comp_ID:
						ques=b1+elt.Can_ID+b2+x.Candidate_Name+b3+x.Institution_Name+b4+x.Course+b5+x.Branch+b6+elt.Marks+b7
						da=da+ques+"\n"
		obj=AddComp.objects.all()
		for elt in obj:
			if a==elt.Comp_ID:
				name=elt.Comp_Name
		context={'ques':da,
		'name':name}
		return render(request,'results.html',context)
def ourteam(request):
	return render(request,"ourteam.html",{})
@csrf_exempt
def query(request):
	if request.method=="POST":
		name=request.POST.get('name')
		email=request.POST.get('email')
		message=request.POST.get('message')
		maill="Name- "+name+"\nEmail- "+email+"\nMessage- "+message+"\n\nThanks & Regards\nStrife Web Server"
		emaill=EmailMessage('User Query',maill,to=['strifeapp99@gmail.com'])
		emaill.send()
		ob=AddComp.objects.all()
		filedata=File.objects.all()
		b1="Hello"
		b2=" "
		b3=" "
		b4=" "
		b5=" "
		b6=" "
		b7=" "
		b8=" "
		b9=" "
		b10=" "
		b11=" "
		b12=" "
		for elt in filedata:
			if elt.FName=="q1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q4":
				b2=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q5":
				b3=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q6":
				b4=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q7":
				b5=elt.FData
				break
		compname=b1
		Status="Y"
		for elt in ob:
			if elt.Status=="Y":
				comp=b2+elt.Comp_Name+b3+elt.Comp_Name+b4
				compname=compname+comp
		compname=compname+b5
		filedata=File.objects.all()
		b1=" "
		b2=" "
		for elt in filedata:
			if elt.FName=="alert1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="alert2":
				b2=elt.FData
				break
		alert=b1+"We have recieved your query. We will respond you soon!"+b2
		context={'compname':compname,
				'alert':alert}
		return render(request,"bout.html",context)
def fileopen(request):
	return render(request,"file.html",{})
@csrf_exempt
def filedata(request):
	if request.method=="POST":
		name=request.POST.get('name')
		data=request.POST.get('data')
		obj=File(FName=name,FData=data)
		obj.save()
		return render(request,"file.html",{})
def remcomp(request):
	return render(request,"removecomp.html",{})
@csrf_exempt
def compdelete(request):
	if request.method=="POST":
		adminemail = request.session['Email']
		compid = request.session['CompID']
		p=request.POST.get('pass')
		ob=NewAdmin.objects.all()
		obj=AddComp.objects.filter(Comp_ID=compid)
		obj1=CompQuiz.objects.filter(Comp_ID=compid)
		obj2=CanData.objects.filter(Comp_ID=compid)
		obj3=CanMarks.objects.filter(Comp_ID=compid)
		for elt in ob:
			if adminemail==elt.Email and p==elt.Password:
				obj.delete()
				obj1.delete()
				obj2.delete()
				obj3.delete()
				break
		filedata=File.objects.all()
		b1="Hello"
		b2=" "
		for elt in filedata:
			if elt.FName=="alert1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="alert2":
				b2=elt.FData
				break
		alert=b1+"Competition Deleted Successfully"+b2
		d=0
		i = request.session['Email']
		obj=NewAdmin.objects.all()
		for elt in obj:
			if i==elt.Email:
				context={'admin':elt.Admin_Name,
						'post':elt.Admin_Post,
						'name':elt.Institution_Name,
						'email':elt.Email,
						'mobile':elt.Mobile,
						'unique':elt.Mobile,
						'alert':alert}
				d=1
				break
		if d==0:
			return render(request,"nouser.html",{})
		else:
			return render(request,'adminprofile.html',context)
@csrf_exempt
def canlist(request):
		filedata=File.objects.all()
		b1=" "
		b2=" "
		b3=" "
		b4=" "
		b5=" "
		b6=" "
		b7=" "
		for elt in filedata:
			if elt.FName=="w1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w2":
				b2=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w3":
				b3=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w4":
				b4=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w5":
				b5=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w6":
				b6=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w7":
				b7=elt.FData
				break
		da="<h1>Hello</h1>"
		a = request.session['CompID']
		obj=CanData.objects.filter(Comp_ID=a)
		for elt in obj:
			ques=b1+elt.Candidate_Name+b2+elt.Can_ID+b3+elt.Institution_Name+b4+elt.Course+b5+elt.Branch+b6+elt.Candidate_Email+b7
			da=da+ques+"\n"
		obj=AddComp.objects.all()
		for elt in obj:
			if a==elt.Comp_ID:
				name=elt.Comp_Name
		context={'ques':da,
		'name':name}
		return render(request,'canlist.html',context)
import csv
def canCSV(request):
		a = request.session['CompID']
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=CandidateList.csv'
		writer = csv.writer(response)
		obj1=CanData.objects.filter(Comp_ID=a)
		obj=AddComp.objects.all()
		writer.writerow(["Competition Name", "Can ID", "Name", "Email", "Course", "Field Of Study", "Institution"])
		for elt in obj:
			if a==elt.Comp_ID:
				name=elt.Comp_Name
				for x in obj1:
					writer.writerow([name, x.Can_ID, x.Candidate_Name, x.Candidate_Email, x.Course, x.Branch, x.Institution_Name])
		return response
def resultsCSV(request):
		a = request.session['CompID']
		obj=AddComp.objects.all()
		for elt in obj:
			if a==elt.Comp_ID:
				name=elt.Comp_Name
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename='+name+'.csv'
		writer = csv.writer(response)
		obj=CanMarks.objects.all()
		obj1=CanData.objects.all()
		writer.writerow(["Can ID", "Name", "Email", "Institute", "Course", "Field Of Study", "Marks"])
		for elt in obj:
			if a==elt.Comp_ID:
				for x in obj1:
					if elt.Can_ID==x.Can_ID:
						writer.writerow([elt.Can_ID, x.Candidate_Name, x.Candidate_Email, x.Institution_Name, x.Course, x.Branch, elt.Marks])
		return response
@csrf_exempt
def adminact(request):
		adminid = request.session['AdminEmail']
		adminpass = request.session['AdminPass']
		ob=NewAdmin.objects.filter(Email=adminid,Password=adminpass).update(Paid="Y")
		return render(request,'adminact.html',{})
def adminactive(request):
		return render(request,'adminact.html',{})
def resetpass(request):
	n = request.session['AdminName']
	return render(request,'resetpassword.html',{'AdminName':n})
@csrf_exempt
def resetpassword(request):
	d=0
	s="Y"
	e = request.session['Email']
	op=request.POST.get('opass')
	np=request.POST.get('npass')
	obj=NewAdmin.objects.filter(Email=e,Password=op).update(Password=np)
	context={}
	filedata=File.objects.all()
	b1="Hello"
	b2=" "
	for elt in filedata:
		if elt.FName=="alert1":
			b1=elt.FData
			break
	for elt in filedata:
		if elt.FName=="alert2":
			b2=elt.FData
			break
	alert=b1+"Your Password has been successfully changed!"+b2
	if obj==0:
		n = request.session['AdminName']
		alert=b1+"Incorrect Password"+b2
		return render(request,'resetpassword.html',{'AdminName':n,'alert':alert})
	obj=NewAdmin.objects.filter(Email=e)
	for elt in obj:
		d=1
		context={'admin':elt.Admin_Name}
		context={'admin':elt.Admin_Name,
				'post':elt.Admin_Post,
				'name':elt.Institution_Name,
				'email':elt.Email,
				'mobile':elt.Mobile,
				'alert':alert}
		break
	if d==0:
		return render(request,"adminnotfound.html",{})
	if d==1:
		return render(request,'adminprofile.html',context)
def deleteQues(request):
	cid = request.session['CompID']
	aid = request.session['Admin_ID']
	ob=CompQuiz.objects.filter(Comp_ID=cid)
	filedata=File.objects.all()
	b1="Hello"
	b2=" "
	b3=" "
	b4=" "
	b5=" "
	for elt in filedata:
		if elt.FName=="q1":
			b1=elt.FData
			break
	for elt in filedata:
		if elt.FName=="q4":
			b2=elt.FData
			break
	for elt in filedata:
		if elt.FName=="q5":
			b3=elt.FData
			break
	for elt in filedata:
		if elt.FName=="q6":
			b4=elt.FData
			break
	for elt in filedata:
		if elt.FName=="q7":
			b5=elt.FData
			break
	compname=b1
	for elt in ob:
		comp=b2+elt.Ques+b3+elt.Ques+b4
		compname=compname+comp
	compname=compname+b5
	name=" "
	obj=AddComp.objects.filter(Comp_ID=cid)
	for elt in obj:
		name=elt.Comp_Name
	context={'quesname':compname,
				'name':name}
	return render(request,'deleteques.html',context)
@csrf_exempt
def deleteQ(request):
	if request.method=="POST":
		c=request.POST.get('compname')
		cid = request.session['CompID']
		aid = request.session['Admin_ID']
		name=" "
		obj=AddComp.objects.filter(Comp_ID=cid)
		for elt in obj:
			name=elt.Comp_Name
			break
		obj=CompQuiz.objects.filter(Comp_ID=cid,Ques=c)
		obj.delete()
		ob=CompQuiz.objects.filter(Comp_ID=cid)
		filedata=File.objects.all()
		b1="Hello"
		b2=" "
		b3=" "
		b4=" "
		b5=" "
		for elt in filedata:
			if elt.FName=="q1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q4":
				b2=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q5":
				b3=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q6":
				b4=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q7":
				b5=elt.FData
				break
		compname=b1
		for elt in ob:
			comp=b2+elt.Ques+b3+elt.Ques+b4
			compname=compname+comp
		compname=compname+b5
		for elt in filedata:
			if elt.FName=="alert1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="alert2":
				b2=elt.FData
				break
		alert=b1+"Deleted Successfully"+b2
		print(alert)
		context={'quesname':compname,
				'alert':alert,
				'name':name}
		return render(request,'deleteques.html',context)
#Super Admin
def superadmin(request):
	return render(request,'superadmin.html',{})
@csrf_exempt
def superadmincheck(request):
	if request.method=="POST":
		d=0
		filedata=File.objects.all()
		b1=" "
		b2=" "
		b3=" "
		b4=" "
		b5=" "
		b6=" "
		b7=" "
		for elt in filedata:
			if elt.FName=="w1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w2":
				b2=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w3":
				b3=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w4":
				b4=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w5":
				b5=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w6":
				b6=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w7":
				b7=elt.FData
				break
		filedata=File.objects.all()
		s1="Hello"
		s2=" "
		s3=" "
		s4=" "
		s5=" "
		for elt in filedata:
			if elt.FName=="q1":
				s1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q4":
				s2=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q5":
				s3=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q6":
				s4=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q7":
				s5=elt.FData
				break
		adminid=s1
		p=request.POST.get('pass')
		adata=" "
		compname=' '
		if p=="@Soviya19971999":
			d=1
			admin=NewAdmin.objects.all()
			for elt in admin:
				ad=b1+elt.Institution_Name+b2+elt.Admin_Name+b3+elt.Admin_Post+b4+elt.Mobile+b5+elt.Email+b6+elt.Paid+b7
				adata=adata+ad
				comp=s2+elt.Mobile+s3+elt.Mobile+s4
				compname=compname+comp
		adminid=adminid+compname+s5
		if d==0:
			return render(request,'superadmin.html',{})
		else:
			context={'adata':adata,
					'adminid':adminid}
			return render(request,'superadminprofile.html',context)
@csrf_exempt
def changepaid(request):
	if request.method=='POST':
		d=0
		id=request.POST.get('compname')
		ob=NewAdmin.objects.filter(Mobile=id)
		for elt in ob:
			if elt.Paid=='Y':
				ob=NewAdmin.objects.filter(Mobile=id).update(Paid="N")
				d=1
			if elt.Paid=='N':
				ob=NewAdmin.objects.filter(Mobile=id).update(Paid="Y")
				d=1
		filedata=File.objects.all()
		b1=" "
		b2=" "
		b3=" "
		b4=" "
		b5=" "
		b6=" "
		b7=" "
		for elt in filedata:
			if elt.FName=="w1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w2":
				b2=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w3":
				b3=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w4":
				b4=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w5":
				b5=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w6":
				b6=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w7":
				b7=elt.FData
				break
		filedata=File.objects.all()
		s1="Hello"
		s2=" "
		s3=" "
		s4=" "
		s5=" "
		for elt in filedata:
			if elt.FName=="q1":
				s1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q4":
				s2=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q5":
				s3=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q6":
				s4=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q7":
				s5=elt.FData
				break
		adminid=s1
		p=request.POST.get('pass')
		adata=" "
		compname=' '
		admin=NewAdmin.objects.all()
		for elt in admin:
			ad=b1+elt.Institution_Name+b2+elt.Admin_Name+b3+elt.Admin_Post+b4+elt.Mobile+b5+elt.Email+b6+elt.Paid+b7
			adata=adata+ad
			comp=s2+elt.Mobile+s3+elt.Mobile+s4
			compname=compname+comp
		adminid=adminid+compname+s5
		context={'adata':adata,
					'adminid':adminid}
		if d==1:
			return render(request,'superadminprofile.html',context)
def getpass(request):
	filedata=File.objects.all()
	s1="Hello"
	s2=" "
	s3=" "
	s4=" "
	s5=" "
	for elt in filedata:
		if elt.FName=="q1":
			s1=elt.FData
			break
	for elt in filedata:
		if elt.FName=="q4":
			s2=elt.FData
			break
	for elt in filedata:
		if elt.FName=="q5":
			s3=elt.FData
			break
	for elt in filedata:
		if elt.FName=="q6":
			s4=elt.FData
			break
	for elt in filedata:
		if elt.FName=="q7":
			s5=elt.FData
			break
	adminid=s1
	compname=' '
	admin=NewAdmin.objects.all()
	for elt in admin:
		comp=s2+elt.Mobile+s3+elt.Mobile+s4
		compname=compname+comp
	adminid=adminid+compname+s5
	context={'adminid':adminid}
	return render(request,'getadminpassword.html',context)
@csrf_exempt
def getadminpassword(request):
	if request.method=='POST':
		d=0
		id=request.POST.get('compname')
		ob=NewAdmin.objects.filter(Mobile=id)
		for elt in ob:
			msg='Hi,\nPassword for Admin Account '+elt.Admin_Name+' with emaid id '+elt.Email+' is '+elt.Password+'\n\nThanks & Regards\nStrife Server'
			email=EmailMessage('Strife Account Recovery',msg,to=['strifeapp99@gmail.com'])
			email.send()
			d=1
		filedata=File.objects.all()
		b1=" "
		b2=" "
		b3=" "
		b4=" "
		b5=" "
		b6=" "
		b7=" "
		for elt in filedata:
			if elt.FName=="w1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w2":
				b2=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w3":
				b3=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w4":
				b4=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w5":
				b5=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w6":
				b6=elt.FData
				break
		for elt in filedata:
			if elt.FName=="w7":
				b7=elt.FData
				break
		filedata=File.objects.all()
		s1="Hello"
		s2=" "
		s3=" "
		s4=" "
		s5=" "
		for elt in filedata:
			if elt.FName=="q1":
				s1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q4":
				s2=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q5":
				s3=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q6":
				s4=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q7":
				s5=elt.FData
				break
		adminid=s1
		p=request.POST.get('pass')
		adata=" "
		compname=' '
		admin=NewAdmin.objects.all()
		for elt in admin:
			ad=b1+elt.Institution_Name+b2+elt.Admin_Name+b3+elt.Admin_Post+b4+elt.Mobile+b5+elt.Email+b6+elt.Paid+b7
			adata=adata+ad
			comp=s2+elt.Mobile+s3+elt.Mobile+s4
			compname=compname+comp
		adminid=adminid+compname+s5
		context={'adata':adata,
					'adminid':adminid}
		if d==1:
			return render(request,'superadminprofile.html',context)
#For Deleting Candidate
def deleteCandidate(request):
	cid = request.session['CompID']
	aid = request.session['Admin_ID']
	ob=CanData.objects.filter(Comp_ID=cid)
	filedata=File.objects.all()
	b1="Hello"
	b2=" "
	b3=" "
	b4=" "
	b5=" "
	for elt in filedata:
		if elt.FName=="q1":
			b1=elt.FData
			break
	for elt in filedata:
		if elt.FName=="q4":
			b2=elt.FData
			break
	for elt in filedata:
		if elt.FName=="q5":
			b3=elt.FData
			break
	for elt in filedata:
		if elt.FName=="q6":
			b4=elt.FData
			break
	for elt in filedata:
		if elt.FName=="q7":
			b5=elt.FData
			break
	compname=b1
	for elt in ob:
		comp=b2+elt.Candidate_Name+b3+elt.Candidate_Name+b4
		compname=compname+comp
	compname=compname+b5
	name=" "
	obj=AddComp.objects.filter(Comp_ID=cid)
	for elt in obj:
		name=elt.Comp_Name
	context={'canname':compname,
				'name':name}
	return render(request,'deletecandidate.html',context)
@csrf_exempt
def deleteCan(request):
	if request.method=="POST":
		c=request.POST.get('compname')
		cid = request.session['CompID']
		aid = request.session['Admin_ID']
		name=" "
		obj=AddComp.objects.filter(Comp_ID=cid)
		for elt in obj:
			name=elt.Comp_Name
			break
		obj=CanData.objects.filter(Comp_ID=cid,Candidate_Name=c)
		obj.delete()
		ob=CanData.objects.filter(Comp_ID=cid)
		filedata=File.objects.all()
		b1="Hello"
		b2=" "
		b3=" "
		b4=" "
		b5=" "
		for elt in filedata:
			if elt.FName=="q1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q4":
				b2=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q5":
				b3=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q6":
				b4=elt.FData
				break
		for elt in filedata:
			if elt.FName=="q7":
				b5=elt.FData
				break
		compname=b1
		for elt in ob:
			comp=b2+elt.Candidate_Name+b3+elt.Candidate_Name+b4
			compname=compname+comp
		compname=compname+b5
		for elt in filedata:
			if elt.FName=="alert1":
				b1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="alert2":
				b2=elt.FData
				break
		alert=b1+"Deleted Successfully"+b2
		print(alert)
		context={'canname':compname,
				'alert':alert,
				'name':name}
		return render(request,'deletecandidate.html',context)
def getpre(request):
	return render(request,"premium.html",{})
@csrf_exempt
def premium(request):
	if request.method=='POST':
		d=0
		i=request.POST.get('id')
		p=request.POST.get('pass')
		obj=NewAdmin.objects.all()
		ob=NewAdmin.objects.filter(Email=i).update(Paid="N")
		ps=0
		context={}
		filedata=File.objects.all()
		al1="Hello"
		al2=" "
		for elt in filedata:
			if elt.FName=="alert1":
				al1=elt.FData
				break
		for elt in filedata:
			if elt.FName=="alert2":
				al2=elt.FData
				break
		for elt in obj:
			if i==elt.Email and p==elt.Password:
				d=1
				context={'admin':elt.Admin_Name}
				if elt.Paid=='N':
					ps=0
					break
		if ps==0 and d==1:
			request.session['AdminEmail'] = request.POST['id']
			request.session['AdminPass'] = request.POST['pass']
			return render(request,"userres.html",context)
		if d==0:
			alert=al1+"Incorrect Email or Password"+al2
			return render(request,'premium.html',{'alert':alert})