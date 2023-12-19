from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'username', 'first_name', 'last_name')   # اى ان عند الضغط عليه هيبقلك للتفاصيل 
    readonly_fields = ('last_login', 'date_joined')     # غير قابل للتعديل وقابل للضغط
    ordering = ('-date_joined',)     

    # Bắt buộc phải khai báo
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)