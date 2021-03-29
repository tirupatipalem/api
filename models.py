from django.db import models



class Course(models.Model):
    c_name = models.CharField(max_length=64,null=True,blank=True)

    def __str__(self):
        return self.c_name


class Subject(models.Model):
    sub_name = models.CharField(max_length=64,null=True,blank=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.sub_name

class Profile(models.Model):
    type = models.CharField(max_length=64,null=True,blank=True)
    course = models.ManyToManyField(Course)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.type


class Results(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    marks = models.FloatField(null=True,blank=True)
    


