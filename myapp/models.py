from django.db import models

class NewAdmin(models.Model):
	Institution_Name=models.CharField(max_length=1000)
	Admin_Name=models.CharField(max_length=100)
	Admin_Post=models.CharField(max_length=100)
	Mobile=models.CharField(max_length=15)
	Email=models.CharField(max_length=100)
	Password=models.CharField(max_length=20)
	Paid=models.CharField(max_length=20)
	class Meta:
		db_table="NewAdmin"
class AddComp(models.Model):
	Comp_ID=models.CharField(max_length=1000)
	Admin_ID=models.CharField(max_length=1000)
	Comp_Name=models.CharField(max_length=1000)
	Cate_Name=models.CharField(max_length=1000)
	About_Comp=models.CharField(max_length=2000)
	Number_Ques=models.IntegerField()
	MaxMarks=models.IntegerField()
	MarksPerQues=models.IntegerField()
	Time=models.IntegerField()
	Status=models.CharField(max_length=20)
	class Meta:
		db_table="AddComp"
class CompQuiz(models.Model):
	Admin_ID=models.CharField(max_length=15)
	Comp_ID=models.CharField(max_length=1000)
	Ques_No=models.CharField(max_length=1000)
	Ques=models.CharField(max_length=10000)
	A=models.CharField(max_length=2000)
	B=models.CharField(max_length=2000)
	C=models.CharField(max_length=2000)
	D=models.CharField(max_length=2000)
	Answer=models.CharField(max_length=5)
	class Meta:
		db_table="CompQuiz"
		
class CanData(models.Model):
	Login_ID=models.CharField(max_length=1000)
	Can_ID=models.CharField(max_length=1000)
	Candidate_Name=models.CharField(max_length=1000)
	Candidate_Email=models.CharField(max_length=1000)
	Comp_ID=models.CharField(max_length=1000)
	Course=models.CharField(max_length=200)
	Branch=models.CharField(max_length=200)
	Institution_Name=models.CharField(max_length=20000)

class CanMarks(models.Model):
	Comp_ID=models.CharField(max_length=1000)
	Can_ID=models.CharField(max_length=1000)
	Marks=models.CharField(max_length=5)
	class Meta:
		db_table="CanMarks"

class File(models.Model):
	FName=models.CharField(max_length=10)
	FData=models.CharField(max_length=100000)
	class Meta:
		db_table="File"