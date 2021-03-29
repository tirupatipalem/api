from django.contrib import admin

# Register your models here.
from . models import Course,Subject,Profile,Results

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','c_name']

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id','sub_name','course']   

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','type']

class ResultsAdmin(admin.ModelAdmin):
    list_display = ['id','user','course','subject','marks']         

admin.site.register(Course,CourseAdmin)    
admin.site.register(Subject,SubjectAdmin)   
admin.site.register(Profile,ProfileAdmin)   
admin.site.register(Results,ResultsAdmin)   