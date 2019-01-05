from django.db import models

# Create your models here.
class Employee(models.Model):
	eno=models.IntegerField()
	ename=models.CharField(max_length=64)
	esal=models.IntegerField()
	eadr=models.CharField(max_length=64)

	def  __str__(self):
	      return self.eno