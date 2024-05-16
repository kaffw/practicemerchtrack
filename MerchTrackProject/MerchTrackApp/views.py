from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import userInfo, order_info, order_details


def home(request):
    return render(request, "index.html")

def trackOrder(request):
    try:
        student_id = request.GET.get('student_id')
        order_details_id = request.GET.get('order_details_id')
        
        orders = order_info.objects.filter(user_info_ID=student_id).values()
        
        
        # order_id = get_by_id(orders)
        
        order_detail = order_details.objects.filter(order_details_ID=orders[0]['id']).values()
        # print("orders.id")
        # print(orders[0]['id'])
        # print("order deets")
        # print(order_detail)
        # order_details = order_info.objects.get(pk=orders.id)

        template = loader.get_template('track_order.html')
        content = {
            'orders': orders,
            'order_details': order_detail,
        }
        print(content)
        return HttpResponse(template.render(content, request))
    except userInfo.DoesNotExist:
        student = None
        return render(request, "index.html", {'error_message': 'student id does not exist'})

def aboutUs(request):
    return render(request, "about_us.html")

def contactUs(request):
    return render(request, "contact_us.html")
















            # dates = {
        #     'order_date': orders,
        #     'distribution_date': orders
        # }