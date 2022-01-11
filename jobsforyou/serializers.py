from rest_framework import serializers
from .models import job

class jobSerializer(serializers.Serializer):
    jobid = serializers.CharField(max_length=20,default="")
    jobtitle = serializers.CharField(max_length=100,default="")
    image = serializers.CharField(max_length=None,default="")
    jobrole = serializers.CharField(max_length=100,default="")
    description = serializers.CharField(max_length=None,default="")
    eligibility = serializers.CharField(max_length=None,default="")
    qualification = serializers.CharField(max_length=None,default="")
    salary = serializers.CharField(max_length=50,default="")
    location = serializers.CharField(max_length=50,default="")
    lastdate = serializers.CharField(max_length=25,default="")
    applylink = serializers.CharField(max_length=None,default="")
    def create(self,validate_data):
        return job.objects.create(**validate_data)


class indexSerializer(serializers.Serializer):
    jobid = serializers.CharField(max_length=10,default="")
    jobtitle = serializers.CharField(max_length=100,default="")
    image = serializers.CharField(max_length=None,default="")