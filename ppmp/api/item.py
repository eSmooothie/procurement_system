"""
UNDER CONSTRUCTION:

READ ABOUT: DJANGO REST FRAMEWORK
"""
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import status

from ppmp.models import Item, ItemCategory, Prices, RequestItem, RequestItemCategory
from ppmp.serializers import ItemCategorySerializer

from babel.numbers import format_currency

def autocomplete_search(request):
    if "cat_code" in request.GET:
        cat_code = request.GET['cat_code']
    else:
        return JsonResponse({"msg":"Invalid request."}, status=status.HTTP_400_BAD_REQUEST)

    keyword = request.GET['term'] if "term" in request.GET else None

    if not ItemCategory.objects.select_related().filter(cat_code=cat_code, item__name__icontains=keyword).exists():
        return JsonResponse({"msg":"No match"}, status=status.HTTP_204_NO_CONTENT)

    items = ItemCategory.objects.select_related().filter(cat_code=cat_code, item__name__icontains=keyword).all()

    serialize = ItemCategorySerializer(items, many=True)
    data = []
    raw_data = serialize.data
    for raw in raw_data:
        item = Item.objects.get(id=raw['item']['id'])
        
        formatted = {
            'id' : item.id,
            'value' : item.name,
            'name' : item.name,
            'unit' : item.unit,
            'price' : format_currency(item.get_price(), 'PHP', locale='en_US')
        }
        data.append(formatted)

    return JsonResponse(data, status=status.HTTP_200_OK, safe=False)


def add_item(request):

    if request.method == 'POST':
        raw_data = request.POST

        item = Item()
        item.name = raw_data['item_name']
        item.unit = raw_data['item_unit']
        item.save()

        price = Prices()
        price.item = item
        price.price = raw_data['item_price']
        price.save()

        for cat in raw_data.getlist('categories[]'):
            item_cat = ItemCategory()
            item_cat.item = item
            item_cat.cat_code = cat
            item_cat.save()

        return JsonResponse({'msg':'OK'}, status=status.HTTP_200_OK)

    return JsonResponse({'msg':'Invalid access'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def req_item(request):
    if request.method == 'POST':
        raw_data = request.POST

        req_item = RequestItem()
        req_item.user = request.user
        req_item.name = raw_data['item_name']
        req_item.unit = raw_data['item_unit']
        req_item.price = raw_data['item_price']
        req_item.save()

        for cat in raw_data.getlist('categories[]'):
            req_cat_item = RequestItemCategory()
            req_cat_item.req_item = req_item
            req_cat_item.cat_code = cat
            req_cat_item.save()

        return JsonResponse({'msg':'OK'}, status=status.HTTP_200_OK)

    return JsonResponse({'msg':'Invalid access'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def approved_req_item(request, item_id):
    
    req_item = RequestItem.objects.get(id=item_id)

    if not req_item.is_approved:
        req_item.is_approved = True
        req_item.save()

        new_item = Item()
        new_item.name = req_item.name
        new_item.unit = req_item.unit
        new_item.save()

        price = Prices()
        price.item = new_item
        price.price = req_item.price
        price.save()

        for cat in req_item.categories:
            item_cat = ItemCategory()
            item_cat.item = new_item
            item_cat.cat_code = cat.cat_code
            item_cat.save()
        

    return redirect('req_item_view')


def get_req_item(request):
    if request.method == 'GET':
        raw_data = request.GET
        item_id = raw_data['item_id']

        req_item = RequestItem.objects.get(id=item_id)

        data = {
            'id' : req_item.id,
            'name' : req_item.name,
            'unit' : req_item.unit,
            'price' : req_item.price
        }
        categories = list()
        for cat in req_item.categories:
            cat_code = cat.category.code
            cat_name = cat.category.name

            categories.append({'code':cat_code, 'name': cat_name})

        data['categories'] = categories

        return JsonResponse(data, status=status.HTTP_200_OK, safe=True)

    return JsonResponse({'msg':'Invalid access'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def update_req_item(request):
    if request.method == 'POST':
        raw_data = request.POST
        print(raw_data)

        req_item = RequestItem.objects.get(id=raw_data['item_id'])
        req_item.name = raw_data['item_name']
        req_item.unit = raw_data['item_unit']
        req_item.price = raw_data['item_price']
        req_item.delete_categories()
        req_item.save()
        
        for cat in raw_data.getlist('categories[]'):
            req_cat_item = RequestItemCategory()
            req_cat_item.req_item = req_item
            req_cat_item.cat_code = cat
            req_cat_item.save()
            
        return JsonResponse({'msg':'OK'}, status=status.HTTP_200_OK)
    return JsonResponse({'msg':'Invalid access'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
