# coding: utf-8
from models import DecalInCart
from django import forms
from django.forms import ModelForm


class DecalInCartForm(ModelForm):
    class Meta:
        model = DecalInCart
        fields = {'cart', 'decal', 'quantity'}