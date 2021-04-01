from django.contrib import admin

# Register your models here.
from . models import User,ForgetPassword

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','password','email','age','gender','address','phone_no']

class ForgetPasswordAdmin(admin.ModelAdmin):
    list_display = ['id','user','otp']

admin.site.register(User,UserAdmin)   
admin.site.register(ForgetPassword,ForgetPasswordAdmin)  
 
