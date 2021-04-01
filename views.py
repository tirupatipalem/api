from django.shortcuts import render
from . models import User
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse,response
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt


from . models import ForgetPassword
from django.core.mail import send_mail


@api_view(['GET'])
def get_api(request):
    if request.method == 'GET':
        user_qs = list(User.objects.all().values())

        return JsonResponse({'success':True,'data':user_qs})
    return JsonResponse({'success':False,'data':'does not exist'})


@api_view(['POST'])
def post_api(request):
    if request.method == 'POST':

        username = request.data.get('username')  
        password = make_password(request.data.get('password'))
        email = request.data.get('email')
        age = request.data.get('age')
        gender = request.data.get('gender')
        address = request.data.get('address')
        phone_no = request.data.get('phone_no')


        if User.objects.filter(username=username).exists():
            return JsonResponse({'success':False,'data':'username already exists'})  

        if User.objects.filter(email=email).exists():
            return JsonResponse({'success':False,'data':'Email already exists'})      

        User.objects.create(username=username,
                            password=password,
                            email=email,
                            age=age,
                            gender=gender,
                            address=address,
                            phone_no=phone_no)

        return JsonResponse({'success':True,'data':'data created Successfully'})
    return JsonResponse({'success':False,'data':'does not exist'})

                    
    
@api_view(['PUT'])
def put_api(request,pk):
    if request.method == 'PUT':

        user_id = pk
        username = request.data.get('username')  
        password = make_password(request.data.get('password'))
        email = request.data.get('email')
        age = request.data.get('age')
        gender = request.data.get('gender')
        address = request.data.get('address')
        phone_no = request.data.get('phone_no')

        User.objects.filter(id=user_id).update(username=username,
                                    password=password,
                                    email=email,
                                    age=age,
                                    gender=gender,
                                    address=address,
                                    phone_no=phone_no)

        return JsonResponse({'success':True,'data':'data updated Successfully'})
    return JsonResponse({'success':False,'data':'does not exist'})

@api_view(['DELETE'])
def delete_api(request,pk):
    if request.method == 'DELETE':

        user_id = pk    
        User.objects.filter(id=user_id).delete()

        return JsonResponse({'success':True,'data':'data deleted Successfully'})
    return JsonResponse({'success':False,'data':'does not exist'})



def authenticate(username=None,password=None):
    user = User.objects.get(username=username)
    return user.check_password(password)

@api_view(['POST'])
@csrf_exempt
def login_api(request):
    if request.method == 'POST':

        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user_ins = User.objects.get(username=username)
        except:       
            return JsonResponse({'success':False,'data':'user does not exist'})

        user = authenticate(username, password)

        if user:

            try:
                token_ins=Token.objects.get(user_id=user_ins.id)
                print(token_ins,'tttttttt')
            except:
                token_ins=Token.objects.create(user_id=user_ins.id)

            usr_lst=list(User.objects.filter(username=username).values())

            return JsonResponse({'success':True,'data':usr_lst,'key':token_ins.key})
        else:
            return JsonResponse({'success':False,'data':'password is incorrect'})         
    return JsonResponse({'success':False,'data':'invalid'})
    
        
        

# @api_view(['POST'])
# def forget_password (request):
#     if request.method == 'POST':
        
#         username = request.data.get('username')
#         otp = request.data.get('otp')   
#         email = request.data.get('email')
#         message = "you requested for password reset : {}".format(otp)
#         to = email
#         send_mail( 'Subject here',message,
#                 'tirupatimbr@gmail.com',[to],fail_silently=False)

#         try:
#             user_ins=User.objects.get(username=username)
#         except:
#             return JsonResponse({'success':False,'data':'user does not exist'})  

#         try:
#             data = ForgetPassword.objects.get(user_id=user_ins.id)
#             data.otp=otp
#             data.save()
#             print(data,'ddddddd')
#         except:    
#             ForgetPassword.objects.create(otp=otp,user=user_ins)

#         return JsonResponse({'success':True,'data':'mail sent'})
#     return JsonResponse({'success':False,'data':'invalid'})   

@api_view(['POST'])
def forget_password (request):
    if request.method == 'POST':
        
        username = request.data.get('username')
        otp = request.data.get('otp')   
        email = request.data.get('email')
        message = "you requested for password reset : {}".format(otp)
        to = email
        send_mail( 'Subject here',message,
                'tirupatimbr@gmail.com',[to],fail_silently=False)

        try:
            user_ins=User.objects.get(username=username)
        except:
            return JsonResponse({'success':False,'data':'user does not exist'})  

        try:
            data = ForgetPassword.objects.get(user_id=user_ins.id)
            data.otp=otp
            data.save()
            print(data,'ddddddd')
        except:    
            ForgetPassword.objects.create(otp=otp,user=user_ins)

        return JsonResponse({'success':True,'data':'mail sent'})
    return JsonResponse({'success':False,'data':'invalid'})   






@api_view(['POST'])
def Reset_api(request):
    if request.method == 'POST':
        otp = request.data.get('otp')
        username = request.data.get('username')
        password = request.data.get('password')

        user_qs = ForgetPassword.objects.filter(user__username=username,otp=otp).exists()
        print(user_qs,'uuuuuuuuu')

        if user_qs:
            User.objects.filter(username=username).update(password=make_password(password))

            return JsonResponse({'success':True,'data':'updated'}) 
        return JsonResponse({'success':False,'data':'username/otp invalid otp'}) 
    return JsonResponse({'success':False,'data':'invalid'})
        



# @api_view(['POST'])
# def Reset_api(request):
#     if request.method == 'POST':
#         otp = request.data.get('otp')
#         username = request.data.get('username')
#         password = request.data.get('password')
#         if username:
#             try:
#                 user_qs = User.objects.get(username=username)
#             except:
#                 return JsonResponse({'success':False,'data':'username does not exist'}) 

#             print(user_qs,'uuuuuuuuuuuuuuuuu')
#             otp_qs = ForgetPassword.objects.get(user=user_qs)
#             if otp == otp_qs.otp:
#                 User.objects.filter(username=username).update(password=make_password(password))

#                 return JsonResponse({'success':True,'data':'updated'})
#             return JsonResponse({'success':True,'data':'invalid otp'}) 
#         return JsonResponse({'success':False,'data':'invalid username'}) 
#     return JsonResponse({'success':False,'data':'invalid'})
        




















