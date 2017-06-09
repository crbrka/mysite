from django.contrib import admin
from .models import *
# Register your models here.


class paymentsAdmin(admin.ModelAdmin):
    list_display = ["id","pay_sum", "pay_datetime","pay_comment"]
    search_fields = ["pay_sum","pay_type","pay_comment"]
    list_filter = ["pay_type","pay_comment"]
    class Meta:
        model = payment


admin.site.register(payment, paymentsAdmin)
