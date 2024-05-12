from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import userInfo

def home(request):
    return render(request, "index.html")

def trackOrder(request):
    student_id = request.GET.get('student_id')

    try:
        student = userInfo.objects.get(student_id=student_id)
        return render(request, "track_order.html")
    except userInfo.DoesNotExist:
        student = None
        return render(request, "index.html", {'error_message': 'student id does not exist'})
