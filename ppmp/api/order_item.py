import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import status

from ppmp.models import OrderDetails

@login_required(login_url='login_user')
def update_ppmp_orderitems(request):
    data = {'msg':"Invalid access"}
    
    if request.method == 'POST':
        json_data = request.POST['data']
        parse_data = json.loads(json_data)

        item_list = parse_data['item_list']
        ppmp_id = parse_data['ppmp_id']
        cat_id = parse_data['cat_id']

        for item in item_list:
            item_id = item['item_id']
            
            order_item_model = OrderDetails.objects.get(ppmp_id=ppmp_id, item_desc__item__category_id=cat_id, item_desc_id=item_id)
            order_item_model.first_quart_quant = item['first']
            order_item_model.second_quart_quant = item['second']
            order_item_model.third_quart_quant = item['third']
            order_item_model.fourth_quart_quant = item['fourth']
            order_item_model.save()

        data = {"msg":"Success"}
        return JsonResponse(data, status=status.HTTP_200_OK)
    return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
