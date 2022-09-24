import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import status

from ppmp.models import ItemDescription, OrderDetails, Ppmp, Prices

@login_required(login_url='login_user')
def update_ppmp_orderitems(request):
    data = {'msg':"Invalid access"}
    
    if request.method == 'POST':
        json_data = request.POST['data']
        parse_data = json.loads(json_data)

        item_list = parse_data['item_list']
        ppmp_id = parse_data['ppmp_id']
        cat_id = parse_data['cat_id']

        item_id_list = list()

        for item in item_list:
            if not bool(item):
                continue

            item_id = item['item_id']
            
            item_id_list.append(item_id)

            if OrderDetails.objects.filter(ppmp_id=ppmp_id, item_desc__item__category_id=cat_id, 
                price_id=item['price_id'], item_desc_id=item_id).exists():

                order_item_model = OrderDetails.objects.get(ppmp_id=ppmp_id, item_desc__item__category_id=cat_id, 
                    price_id=item['price_id'], item_desc_id=item_id)

                order_item_model.first_quart_quant = item['first'] if float(item['first']) >= 0 else 0
                order_item_model.second_quart_quant = item['second'] if float(item['second']) >= 0 else 0
                order_item_model.third_quart_quant = item['third'] if float(item['third']) >= 0 else 0
                order_item_model.fourth_quart_quant = item['fourth'] if float(item['fourth']) >= 0 else 0
                order_item_model.save()

            else:
                new_order_item = OrderDetails()
                
                item_desc = ItemDescription.objects.get(pk=item_id)
                ppmp = Ppmp.objects.get(pk=ppmp_id)
                price = Prices.objects.get(pk=item['price_id'])

                new_order_item.item_desc = item_desc
                new_order_item.price = price
                new_order_item.ppmp = ppmp

                new_order_item.first_quart_quant = item['first'] if float(item['first']) >= 0 else 0
                new_order_item.second_quart_quant = item['second'] if float(item['second']) >= 0 else 0
                new_order_item.third_quart_quant = item['third'] if float(item['third']) >= 0 else 0
                new_order_item.fourth_quart_quant = item['fourth'] if float(item['fourth']) >= 0 else 0

                new_order_item.save()

        
        # get all current orderitems under the ppmp
        curr_orderitems = OrderDetails.objects.filter(ppmp_id=ppmp_id, item_desc__item__category_id=cat_id).all()

        #check every item if its in the updated item_list
        for item in curr_orderitems:
            if str(item.item_desc.id) not in item_id_list:
                print(item.item_desc.id)
                item.delete()
            
        data = {"msg":"Success"}
        return JsonResponse(data, status=status.HTTP_200_OK)
    return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
