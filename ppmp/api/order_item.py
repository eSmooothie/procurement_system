import json
import random as rand
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import status
from django.contrib import messages
from ppmp.models import Item, OrderDetails, Ppmp, PpmpTrack, Prices, ProcurementMode, PurchaseRequest

INVALID_REQUEST = {'msg':"Invalid request"}
INVALID_ACCESS = {'msg':"Invalid access"}

@login_required(login_url='login_user')
def put_ppmp_orderitems(request):
    
    if request.method == 'POST' and 'data' in request.POST:
        json_data = request.POST['data']
        parse_data = json.loads(json_data)

        ppmp_id = parse_data['ppmp_id']
        cat_code = parse_data['cat_code']
        items = parse_data['items']

        updated_ordereditems = []

        # adding/updating part
        for item in items:
            updated_ordereditems.append(item['item_id'])

            if 'order_id' in item and OrderDetails.objects.filter(id=item['order_id']).exists():
                order_item = OrderDetails.objects.get(id=item['order_id'])
                order_item.first_quant = item['1']
                order_item.second_quant = item['2']
                order_item.third_quant = item['3']
                order_item.fourth_quant = item['4']

                order_item.save()
            else:
                new_order_item = OrderDetails()

                item_data = Item.objects.get(id=item['item_id'])
                ppmp_data = Ppmp.objects.get(id=ppmp_id)
                
                new_order_item.item = item_data
                new_order_item.ppmp = ppmp_data
                new_order_item.cat_code = cat_code

                new_order_item.first_quant = item['1']
                new_order_item.second_quant = item['2']
                new_order_item.third_quant = item['3']
                new_order_item.fourth_quant = item['4']

                new_order_item.save()

        # removing part
        curr_ordereditems = OrderDetails.objects.select_related().filter(ppmp__id=ppmp_id, cat_code=cat_code).all()

        for orderitem in curr_ordereditems:
            # check if item is in the updated item list
            if str(orderitem.item.id) not in updated_ordereditems:
                orderitem.delete()

        data = {"msg":"Success"}
        return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
    return JsonResponse(INVALID_ACCESS, status=status.HTTP_400_BAD_REQUEST)

def generate_code(item_id):
    rand_number = rand.randint(1, 9999999)
    code = str(rand_number) + str(item_id)
    return hash(code)

def get_orderitem_logs(request):
    
    if request.method == 'GET' and 'orderitem_id' in request.GET:
        orderitem_id = request.GET['orderitem_id']

        orderdetail_log = PpmpTrack.objects.select_related().filter(orderdetails_id=orderitem_id).order_by('id').all()

        if not PpmpTrack.objects.select_related().filter(orderdetails_id=orderitem_id).exists():
            orderdetail = OrderDetails.objects.get(id=orderitem_id)
            log_records = []
            data = {
                'id' : orderitem_id,
                'item_name' : orderdetail.item.name,
                'status' : {
                    'app' : orderdetail.app_status,
                    'received_quotation' : orderdetail.received_quotation_status,
                    'award_winning' : orderdetail.award_winning_bidder_status,
                    'obligate_po' : orderdetail.obligate_po_status,
                    'served' : orderdetail.served_status
                },
                'log_records' : log_records
            }
            return JsonResponse(data, status=status.HTTP_200_OK) 

        log_records = []

        for log in orderdetail_log:
            log_record = {
                'id' : log.id,
                'datetime' : log.datetime,
                'cc_name' : log.cc_name,
                'barcode' : log.barcode
            }

            log_records.append(log_record)

        orderdetail = orderdetail_log[0].orderdetails #get the detail


        data = {
            'id' : orderitem_id,
            'item_name' : orderdetail.item.name,
            'status' : {
                'app' : orderdetail.app_status,
                'received_quotation' : orderdetail.received_quotation_status,
                'award_winning' : orderdetail.award_winning_bidder_status,
                'obligate_po' : orderdetail.obligate_po_status,
                'served' : orderdetail.served_status
            },
            'log_records' : log_records
        }

        return JsonResponse(data, status=status.HTTP_200_OK)

    return JsonResponse(INVALID_REQUEST, status=status.HTTP_400_BAD_REQUEST)

def get_orderitem(request):
    pass

def post_orderitem_track(request):
    pass

def put_purchase_request(request):
    if request.method == 'POST':
        raw_data = request.POST
        
        order_detail = OrderDetails.objects.get(id=raw_data['order_id'])

        if order_detail.purchase_request:
            purchase_request = order_detail.purchase_request
        else:
            purchase_request = PurchaseRequest()

        purchase_request.specification_details = raw_data['item_name']
        purchase_request.purpose = raw_data['item_purpose']
        purchase_request.unit_cost = raw_data['item_price']
        purchase_request.qty = raw_data['item_qty']
        purchase_request.order_details = order_detail
        purchase_request.save()
        
        messages.success(request, "Purchase Request Save")
        return JsonResponse({'msg':'success'}, status=status.HTTP_201_CREATED)
    messages.error(request, "Purchase Request Fail")
    return JsonResponse({'msg':'Invalid Access.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 