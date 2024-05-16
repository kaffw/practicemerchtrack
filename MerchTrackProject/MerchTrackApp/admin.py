from django.contrib import admin
from .models import userInfo, order_info, order_details
# Register your models here.

admin.site.register(userInfo)
admin.site.register(order_info)
admin.site.register(order_details)