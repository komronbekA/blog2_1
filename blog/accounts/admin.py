from django.contrib import admin
from django.contrib.auth.admin import UserAdmin #admin class
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser  #chaqirib olyapmiz fayillarni 

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'age', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('age',)}),
    )
# foydalanadigan narsalarni yozdim
admin.site.register(CustomUser, CustomUserAdmin)
# admin faylda korinishi uchun admin qoshyapmiz

# Register your models here.
