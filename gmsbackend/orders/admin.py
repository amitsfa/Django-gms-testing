from django.contrib import admin
from .models import order
# Register your models here.


@admin.register(order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'championship', 'amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')