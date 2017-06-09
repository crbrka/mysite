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

class MyAdminSite(AdminSite):
    site_title = ugettext_lazy('My2 site admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('My 2administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site2 administration')

admin.site.register(payment, paymentsAdmin)
admin.site.register(payment_category,payment_categoryAdmin)
