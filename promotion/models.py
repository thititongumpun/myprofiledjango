from django.db import models

# Create your models here.
class experience(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	address = models.CharField(max_length=100)
	dob = models.DateField(max_length=8)
	mobile = models.CharField(max_length=10)
	email = models.EmailField(max_length=100)
	education = models.CharField(max_length=200)
	exp = models.CharField(max_length=200)
	ability = models.CharField(max_length=5000)
	lang = models.CharField(max_length=100)
	interest = models.CharField(max_length=1000)
	resp = models.CharField(max_length=5000)

	def __str__(self):
		return self.name

class sample(models.Model):
	name = models.CharField(max_length=100)
	work = models.CharField(max_length=1000)
	work2 = models.CharField(max_length=1000)
	work3 = models.CharField(max_length=1000)
	work4 = models.CharField(max_length=1000)
	work5 = models.CharField(max_length=5000)
	sskill = models.CharField(max_length=5000)

	def __str__(self):
		return self.name





