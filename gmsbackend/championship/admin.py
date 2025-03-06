from django.contrib import admin
from .models import championship, sports
# Register your models here.
@admin.register(championship)
class championshipAdmin(admin.ModelAdmin):
    list_display = ('name','start_date','end_date')
    filter_horizontal = ('sport',)

@admin.register(sports)
class sportsAdmin(admin.ModelAdmin):
    list_display = ('name',)

