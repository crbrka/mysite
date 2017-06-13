from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


class paymentsAdmin(admin.ModelAdmin):
    list_display = ["id","pay_sum", "pay_datetime","pay_comment"]
    search_fields = ["pay_sum","pay_type","pay_comment"]
    list_filter = ["pay_type","pay_comment"]
    class Meta:
        model = payment

class payment_categoryAdmin(admin.ModelAdmin):
    list_display = ["id","cat_name", "cat_fullname","cat_createtime"]
    search_fields = ["cat_name","cat_fullname"]
    list_filter = ["cat_name","cat_fullname"]
    class Meta:
        model = payment_category

class upper_menuAdmin(admin.ModelAdmin):
    list_display = ["menu_name","menu_link"]
    search_fields = ["menu_name"]
    class Meta:
        model = upper_menu

admin.site.register(payment, paymentsAdmin)
admin.site.register(payment_category,payment_categoryAdmin)
admin.site.register(upper_menu,upper_menuAdmin)
