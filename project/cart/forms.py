# coding: utf-8
from django import forms
from models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'phone', 'email', 'city', 'address', 'payment_type',)
        widgets = {
            'email': EmailWidget,
            'phone': TelWidget,
            'city': HeavySelect2Widget(select2_options={'width': '100%', 'closeOnSelect': True, 'multiple': False},
                                       data_url='/ajax/city/'),
            'payment_type':  forms.RadioSelect(),
            'referral': forms.HiddenInput()
        }