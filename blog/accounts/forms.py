from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
# user creat user yaratish user change user tahrirlash yani o'zgartirish 
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age',)
        # userni yaratish royhatdan otish

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age',)
        # royhatdan otgan odam ozgartirishi mumkun
        