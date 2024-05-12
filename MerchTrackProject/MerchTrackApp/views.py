from django.shortcuts import render, HttpResponse
from .models import userInfo

def home(request):
    return render(request, "index.html")
    # return HttpResponse("Welcome to MerchTrack")

def trackOrder(request):
    #student_id = request.POST.get('student_id')
    student_id = request.GET.get('student_id')

    if student_id:
        try:
            # Query only for student_id, not both student_id and student_name
            student = userInfo.objects.get(student_id=student_id)
            return render(request, "track_order.html")
        except userInfo.DoesNotExist:
            student = None
            return render(request, "index.html")

    else:
        student = None
        return render(request, "index.html")
