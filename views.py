from django.shortcuts import render
from . models import Restaurant,Place,Items
from django.http import response,JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status




@api_view(['GET'])
def test_api(request):
    if request.method == 'GET':
        data = list(Restaurant.objects.all().values())
        # print(data)
        for rest in data:
            place = list(Place.objects.filter(restaurant_id=rest['id']).values())
 
            items = list(Items.objects.filter(restaurant_id=rest['id']).values())
            # print(items)
            rest['places'] = place
            rest['items'] = items
        return JsonResponse({'success':True,'data':data})


@api_view(['POST'])
def restaurant_post(request):
    if request.method == 'POST':
        
        user_id=request.data.get('id')
        r_name = request.data.get('r_name')
        adr = request.data.get('adr')
        i_name = request.data.get('i_name')

        r=Restaurant.objects.create(r_name=r_name)
        Place.objects.create(adr=adr,restaurant_id=r.id)
        Items.objects.create(i_name=i_name,restaurant_id=r.id)

        return JsonResponse({'success':'True','data':'data created'})


#with out pk for updating 

@api_view(['PUT'])
def restaurant_update(request):
    if request.method == 'PUT':

        print(request.data)
        r_name = request.data.get('r_name')
        adr = request.data.get('adr')
        i_name = request.data.get('i_name')
        
        r_id=request.data.get('restaurant_id')
        print(r_id,'r_id')
        Restaurant.objects.filter(id=r_id).update(r_name=r_name)

        p_id = request.data.get('place_id')
        Place.objects.filter(id=p_id).update(adr=adr,restaurant_id=r_id)


        i_id = request.data.get('item_id')
        print(i_id)


#   only for one object

        # i = Items.objects.get(id=i_id)
        # print(i,'i_id')
        # i.i_name=i_name
        # i.save()
        # print(i_name,'iitem')
           
        Items.objects.filter(id=i_id).update(i_name=i_name,restaurant_id=r_id)
    return JsonResponse({'success':True,'data':'data updated'})




# with pk for updating

# @api_view(['PUT'])
# def restaurant_update(request,pk):
#     if request.method == 'PUT':

#         user_id = pk
#         r_name = request.data.get('r_name')

#         adr = request.data.get('adr')
#         place_id = request.data.get('place_id')

#         i_name = request.data.get('i_name')
#         i_id = request.data.get('item_id')
        
#         print(request.data)
#         print(user_id,'id')

#         r=Restaurant.objects.get(id=user_id)
#         print(r,'rest')
#         r.r_name = r_name
#         r.save()
#         print(r,'jgfhhjk')
        
#         Place.objects.filter(id=place_id).update(adr=adr,restaurant_id=r.id)

#         Items.objects.filter(id=i_id).update(i_name=i_name,restaurant_id=r.id)
#     return JsonResponse({'success':True,'data':'data updated'})
        


@api_view(["DELETE"])
def restaurant_delete(request,pk):
    if request.method == 'DELETE':
        user_id=pk
        Restaurant.objects.filter(id=user_id).delete()
        return JsonResponse({'success':True,'data':'data deleted'})
        

#  for single list of dict

@api_view(['GET'])
def get_api(request):
    if request.method == 'GET':
        data = list(Restaurant.objects.all().values())
        # print(data[0]['r_name'])
        for rest in data:
            place = list(Place.objects.filter(restaurant_id=rest['id']).values())
 
            it = list(Items.objects.filter(restaurant_id=rest['id']).values())
       
            rest['places'] = place
            rest['items'] = it
            # print(it)
            # print(place)
            print(rest)

            for i in rest:
                print(i)

        
        return JsonResponse({'success':True,'data':data})
















