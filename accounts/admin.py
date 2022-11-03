from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Investment, UserInvestment, Withdrawals, FAQ


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [ 'username','first_name','last_name','email','code','recommended_by']
    fieldsets = (
        (None, {
            'fields': ("first_name", "last_name", 'initial_balance', 'current_balance', "username", "email", "address", "code",'recommended_by')
        }),
    )

class InvestmentAdmin(UserAdmin):
    model = Investment
    list_display = ['investment', 'deposit', 'payment_mode']



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Investment)
admin.site.register(UserInvestment)
admin.site.register(Withdrawals)
admin.site.register(FAQ)
