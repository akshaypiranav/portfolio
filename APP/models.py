from django.db import models
import os
import datetime
def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)
class Projects(models.Model):
    projectName=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)
    link=models.CharField(max_length=100)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    class Meta:
        db_table='datas'
class ResumeModel(models.Model):
    resume_file = models.FileField(upload_to='resume_files/')  
     