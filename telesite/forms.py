from django import forms
from .models import *


class AddPaymentForm(forms.ModelForm):
    class Meta:
        model = payment
        exclude = ["pay_datetime"]
