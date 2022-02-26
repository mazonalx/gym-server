from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    form = CustomUserChangeForm
    ordering = ('created_at', 'updated_at')
    search_fields = ('email','username','first_name','last_name')
    list_display = ('email','username','first_name','last_name','is_active','is_staff')
    list_filter = ('email','username','first_name','last_name','is_active','is_staff')
    fieldsets = (
        (None, {'fields':('email','username','first_name','last_name','password')}),
        ('Permissions',{'fields':('is_staff','is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username','first_name','last_name',
                       'password1','password2','is_staff','is_active')
        }),
    )
    

admin.site.register(CustomUser,CustomUserAdmin)

