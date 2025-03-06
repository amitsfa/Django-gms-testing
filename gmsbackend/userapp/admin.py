from django.contrib import admin
from .models import User, Athlete, School

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_athlete', 'is_school')
    list_filter = ('is_athlete', 'is_school')

@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'age', 'school_name', 'place')
    search_fields = ('first_name', 'last_name', 'school_name')

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('user', 'person_name', 'school_name', 'place')
    search_fields = ('person_name', 'school_name')

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('user', 'championship', 'sports', 'total_payment', 'status', 'created_at')
#     list_filter = ('status', 'created_at')
#     search_fields = ('user__username', 'championship__name')      