from django.shortcuts import render
from .forms import AddPaymentForm
from .models import *
from django.http import HttpResponse


def index(request):
    query_result = payment_category.objects.all()
    AddPaymentHTMLForm = AddPaymentForm(request.POST or None)
    if request.method == "POST":
        if AddPaymentHTMLForm.is_valid():
            print(request.POST)
            data_form = AddPaymentHTMLForm.save()
            data_form.save()
    return render(request, 'telesite/landing.html', locals())
