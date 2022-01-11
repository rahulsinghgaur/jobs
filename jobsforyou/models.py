from django.db import models

# Create your models here.
class job(models.Model):
    jobid = models.CharField(max_length=20,default="")
    jobtitle = models.CharField(max_length=100,default="")
    image = models.TextField(default="")
    jobrole = models.CharField(max_length=100,default="")
    description = models.TextField(default="")
    eligibility = models.TextField(default="")
    qualification = models.TextField(default="")
    salary = models.CharField(max_length=50,default="")
    location = models.CharField(max_length=50,default="")
    lastdate = models.CharField(max_length=25,default="")
    applylink = models.TextField(default="")