from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("track-order/", views.trackOrder, name="trackOrder")
]