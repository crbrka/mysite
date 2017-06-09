from django.shortcuts import render
from .forms import AddPaymentForm
from django.http import HttpResponse


def index(request):
    var_hello = 'Hello'
    var_world = 'World'
    AddPaymentHTMLForm = AddPaymentForm(request.POST or None)
    if request.method == "POST":
        print(request.POST)
        data_form = AddPaymentHTMLForm.save(commit=False)
        data_form.save()
    return render(request, 'telesite/landing.html', locals())


def help1(request):
    return HttpResponse("Hello u r at help page")