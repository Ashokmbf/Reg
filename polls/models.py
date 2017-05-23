from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class course(models.Model):
	id = models.AutoField(primary_key=True)
	first_name=models.CharField(max_length=50, null=True)
	name = models.CharField(max_length=50, null=False, error_messages = {'required' : "Please enter an name.",})
	email = models.EmailField(max_length=70,null=True,  unique= True)
	password = models.CharField(max_length=50)
	views = (
		(1, 'male'),
		(2, 'female'),
		(3,'others'))
	gender = models.IntegerField(choices=views,null=True)
	course = (
		('1','Java'),
		('2','Python'),
		('3','Android'))
	intrest=models.CharField(max_length=50,choices=course,null=True)
	nation= (
		(1, 'India'),
		(2, 'Australia'),
		(3,'America'),
		(4,'Paris'))
	country=models.IntegerField(choices=nation ,null=True)


