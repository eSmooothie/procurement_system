import json
import random as rand
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import status

from ppmp.models import ItemDescription, OrderDetails, Ppmp, PpmpTrack, Prices

INVALID_REQUEST = {'msg':"Invalid request"}
INVALID_ACCESS = {'msg':"Invalid access"}

@login_required(login_url='login_user')
def put_ppmp_orderitems(request):
    
    if request.method == 'POST' and 'data' in request.POST:
        json_data = request.POST['data']
        parse_data = json.loads(json_data)

        item_list = parse_data['item_list']
        ppmp_id = parse_data['ppmp_id']
        cat_id = parse_data['cat_id']

        item_id_list = list()

        for item in item_list:
            # check if not empty
            if not bool(item):
                continue

            item_id = item['item_id']
            
            item_id_list.append(item_id)

            if OrderDetails.objects.filter(ppmp_id=ppmp_id, item_desc__item__category_id=cat_id, 
                price_id=item['price_id'], item_desc_id=item_id).exists():
                # if order item already exist, update it's new data

                order_item_model = OrderDetails.objects.get(ppmp_id=ppmp_id, item_desc__item__category_id=cat_id, 
                    price_id=item['price_id'], item_desc_id=item_id)

                order_item_model.first_quart_quant = item['first'] if float(item['first']) >= 0 else 0
                order_item_model.second_quart_quant = item['second'] if float(item['second']) >= 0 else 0
                order_item_model.third_quart_quant = item['third'] if float(item['third']) >= 0 else 0
                order_item_model.fourth_quart_quant = item['fourth'] if float(item['fourth']) >= 0 else 0
                order_item_model.save()

            else:
                # if new order item
                new_order_item = OrderDetails()
                
                item_desc = ItemDescription.objects.get(pk=item_id) # get the item
                ppmp = Ppmp.objects.get(pk=ppmp_id) # get the ppmp
                price = Prices.objects.get(pk=item['price_id']) # get the item price

                new_order_item.item_desc = item_desc
                new_order_item.price = price
                new_order_item.ppmp = ppmp

                last_id = OrderDetails.objects.latest('id').id
                new_order_item.qr_code = generate_code(last_id + 1)

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
    return JsonResponse(INVALID_ACCESS, status=status.HTTP_400_BAD_REQUEST)

def generate_code(item_id):
    rand_number = rand.randint(1, 9999999)
    code = str(rand_number) + str(item_id)
    return hash(code)

def get_orderitem_logs(request):
    
    if request.method == 'GET' and 'orderitem_id' in request.GET:
        orderitem_id = request.GET['orderitem_id']

        orderdetail_log = PpmpTrack.objects.select_related().filter(orderdetails_id=orderitem_id).order_by('id').all()

        log_records = []

        for log in orderdetail_log:
            log_record = {
                'id' : log.id,
                'datetime' : log.datetime,
                'cc_name' : log.cc_name,
                'barcode' : log.barcode
            }

            log_records.append(log_record)

        item_name = orderdetail_log[0].orderdetails.item_desc.item.general_name

        if orderdetail_log[0].orderdetails.item_desc.spec_1 != 'None':
            item_name += ' - ' + orderdetail_log[0].orderdetails.item_desc.spec_1
        if orderdetail_log[0].orderdetails.item_desc.spec_2 != 'None':
            item_name += ' - ' + orderdetail_log[0].orderdetails.item_desc.spec_2
        if orderdetail_log[0].orderdetails.item_desc.spec_3 != 'None':
            item_name += ' - ' + orderdetail_log[0].orderdetails.item_desc.spec_3
        if orderdetail_log[0].orderdetails.item_desc.spec_4 != 'None':
            item_name += ' - ' + orderdetail_log[0].orderdetails.item_desc.spec_4
        if orderdetail_log[0].orderdetails.item_desc.spec_5 != 'None':
            item_name += ' - ' + orderdetail_log[0].orderdetails.item_desc.spec_5

        data = {
            'id' : orderitem_id,
            'item_name' : item_name,
            'status' : {
                'app' : orderdetail_log[0].orderdetails.app_status,
                'received_quotation' : orderdetail_log[0].orderdetails.received_quotation_status,
                'award_winning' : orderdetail_log[0].orderdetails.award_winning_bidder_status,
                'obligate_po' : orderdetail_log[0].orderdetails.obligate_po_status,
                'served' : orderdetail_log[0].orderdetails.served_status
            },
            'log_records' : log_records
        }

        return JsonResponse(data, status=status.HTTP_200_OK)

    return JsonResponse(INVALID_REQUEST, status=status.HTTP_400_BAD_REQUEST)

def get_orderitem(request):
    pass

def post_orderitem_track(request):
    pass