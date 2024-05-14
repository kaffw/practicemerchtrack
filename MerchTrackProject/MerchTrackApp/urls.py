from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("track-order/", views.trackOrder, name="trackOrder"),
    path("about-us/", views.aboutUs, name="aboutUs"),
    path("contact-us/", views.contactUs, name="contactUs")
]