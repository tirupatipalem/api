from django.shortcuts import render

# Create your views here.
from . models import Results,Course,Subject,Profile
from django.http import JsonResponse,response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_st(request):
    if request.method == 'GET':
        user_qs = list(Profile.objects.all().values())

        user_li = []
        for user in user_qs:
            course_qs=list(Course.objects.all().values())
            
            course_li=[]
            for course in course_qs:
                subject_qs = list(Subject.objects.filter(course_id =course["id"]).values())
                
                res_li= []
                for subject in subject_qs:
                    results = list(Results.objects.filter(subject_id = subject["id"],course_id = course["id"],user_id= user["id"]).values())
        
                    for res in results:
                        dic={}
                        dic["subject"] = subject["sub_name"]
                        dic["marks"] = res["marks"]
                        
                        res_li.append(dic)
                    
                dic={}
                dic["course_name"] = course["c_name"]
                dic["subjects"] = res_li
                
                if res_li:
                    course_li.append(dic)
                    print(course_li)

            dic={}
            dic["name"] = user["type"]
            dic["course"] = course_li
            if course_li:
                user_li.append(dic)

        return JsonResponse({'sucess':True,'data':user_li})
    return JsonResponse({'success':False,'data':'data does not exist'})    


@api_view(['GET'])
def get_st1(request):
    if request.method == 'GET':
        res_qs = list(Results.objects.all().values("id","user_id","user__type","course__c_name","course_id","subject_id","subject__sub_name","marks"))
        lst = []
        user_lst = []
        for item in res_qs:
            out = { }
            if item['user__type'] not in user_lst:
                out['username'] = item['user__type']
                user_lst.append(item['user__type'])
                lst.append(out)
        for d in lst:
            c_lst = []
            for obj in res_qs:
                if d['username'] == obj['user__type']:
                    c_lst.append(obj)
            d['courses'] = c_lst




        # res_li=[]
        # user_li = [] #2
     
        # for i in res_qs:
        #     dic={}
        #     if i['user_id'] not in user_li:
        #         dic['profile_name'] = i['user__type']
        #         user_li.append(i['user_id'])

        #         dic1 = {}
        #         course_li=[]
        #         dic1['course_name'] = i['course__c_name']
        #         course_li.append(dic1)
        #         dic['courses'] = course_li
        #         print(dic,'cccccccc')

     
        #     else:

        #         dic1 = {}
        #         dic1['course_name'] = i['course__c_name']
        #         print(res_li[user_li.index(i['user_id'])],'jjjjjjjj')
                
        #         res_li[user_li.index(i['user_id'])]['courses'].append(dic1)

        #         res_li.append(dic)



 
         
        return JsonResponse({'sucess':True,'data':lst})
    return JsonResponse({'success':False,'data':'data does not exist'})    

    

            # dic1={}
            
            # if i['course_id'] not in course_li:
            #     dic1['course_name'] = i['course__c_name']
            #     course_li.append(i['course_id'])   
            #     res_li.append(dic1)
                
            #     dic2 = {}
            #     sub_res_li = []
            #     dic2['subject_name'] = i['subject__sub_name']
            #     dic2['marks'] = i['marks']
            #     sub_res_li.append(dic2)
            #     dic1['subjects'] = sub_res_li    

            # else:

            #     dic2 = {}
            #     dic2['subject_name'] = i['subject__sub_name']
            #     dic2['marks'] = i['marks']
            #     # print(res_li[course_li.index(i['course_id'])])

            #     res_li[course_li.index(i['course_id'])]['subjects'].append(dic2)


            
 





            
            


# @api_view(['GET'])
# def get_st(request):
#     if request.method == 'GET':
#         # res_qs = list(Results.objects.all().values())
#         user_qs = list(Profile.objects.all().values())

#         user_li = []
#         for user in user_qs:
#             course_qs=list(Course.objects.all().values())
            
#             course_li=[]
#             for course in course_qs:
#                 subject_qs = list(Subject.objects.filter(course_id =course["id"]).values())
                
#                 res_li= []
#                 for subject in subject_qs:
#                     results = list(Results.objects.filter(subject_id = subject["id"],course_id = course["id"],user_id= user["id"]).values())

                    
#                     for res in results:
                    
#                         dic={}
#                         dic["subject"] = subject["sub_name"]
#                         dic["marks"] = res["marks"]                
#                         res_li.append(dic)
                    
#                 dic={}
#                 dic["course_name"] = course["c_name"]
#                 dic["subjects"] = res_li

#                 d={}
#                 s = 0
#                 for d in res_li:
#                     s=s+d['marks']   
#                 dic["total_marks"] = s
#                 try:
#                     dic["total_percentage"] = (s/(len(res_li)*100))*100
#                 except:
#                     dic["total_percentage"] = 0



#                 if res_li:
#                     course_li.append(dic)
              

#             dic={}
#             dic["name"] = user["type"]
#             dic["course"] = course_li
#             if course_li:
#                 user_li.append(dic)

#         return JsonResponse({'sucess':True,'data':user_li})
#     return JsonResponse({'success':False,'data':'data does not exist'})    





# @api_view(['GET'])
# def get_st1(request):
#     if request.method == 'GET':
#         res_qs = list(Results.objects.all().values("id","user_id","user__type","course__c_name","course_id","subject_id","subject__sub_name","marks"))
        
#         res_li=[]
#         user_li = []
#         course_li=[]
#         for i in res_qs:
#             dic={}
#             if i['user_id'] not in user_li:
#                 dic['profile_name'] = i['user__type']
#                 user_li.append(dic)

#             dic1={}
            
#             if i['course_id'] not in course_li:
#                 dic1['course_name'] = i['course__c_name']
#                 course_li.append(i['course_id'])   
#                 res_li.append(dic1)
                
#                 dic2 = {}
#                 sub_res_li = []
#                 dic2['subject_name'] = i['subject__sub_name']
#                 dic2['marks'] = i['marks']
#                 sub_res_li.append(dic2)
#                 dic1['subjects'] = sub_res_li    

#             else:

#                 dic2 = {}
#                 dic2['subject_name'] = i['subject__sub_name']
#                 dic2['marks'] = i['marks']
#                 # print(res_li[course_li.index(i['course_id'])])

#                 res_li[course_li.index(i['course_id'])]['subjects'].append(dic2)


#         res_li.append(dic)    
          
#         return JsonResponse({'sucess':True,'data':res_li})
#     return JsonResponse({'success':False,'data':'data does not exist'})   


  
   

                
                
