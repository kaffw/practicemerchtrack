from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import userInfo, order_info, order_details


def home(request):
    return render(request, "index.html")

def trackOrder(request):
    try:
        student_id = request.GET.get('student_id')

        orders = order_info.objects.filter(user_info_ID=student_id).values()
        
        order_detail = order_details.objects.filter(order_details_ID=orders[0]['id']).values()

        template = loader.get_template('track_order.html')
        content = {
            'orders': orders,
            'order_details': order_detail,
        }
        
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