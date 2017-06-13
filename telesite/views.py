from django.shortcuts import render
from .forms import AddPaymentForm
from .models import payment_category


def index(request):
    query_result = payment_category.objects.all() #вытягиваем из базы все категории
    AddPaymentHTMLForm = AddPaymentForm(request.POST or None)
    if request.method == "POST":
        if AddPaymentHTMLForm.is_valid():
            print(request.POST)
            data_form = AddPaymentHTMLForm.save()
            data_form.save()
    return render(request, 'telesite/new_item.html', locals())
