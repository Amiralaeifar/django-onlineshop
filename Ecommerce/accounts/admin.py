from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserChangeForm, UserCreationFrom
from .models import User, OtpCode


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'created')


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationFrom
    
    list_display = ('full_name', 'email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    
    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'phone_number', 'password')}),
        ('permissions', {'fields': ('is_admin', 'is_active', 'last_login')})
    )
    
    add_fieldsets = (
        (None, {'fields': ('full_name', 'email', 'phone_number', 'password1', 'password2')}),
    )
    
    search_fields = ('full_name', 'email')
    ordering = ('full_name',)
    filter_horizontal = ()
    
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuser'].disabled = True
        return True
    
        
    
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
