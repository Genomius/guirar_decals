# coding: utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from catalog.models import Decal
from models import Cart, Order


def cart(request):
    if request.method == 'POST':
        if request.is_ajax():
            decal = Decal.objects.get(id=request.POST['decal_id'])
            add_to_cart(request, decal.id, 1)
        else:
            pass
    else:
        decals = Decal.objects.all()

        return render_to_response(
            'cart.html',
            {
                'cart': Cart(request),
                'decals': decals,
            },
            context_instance=RequestContext(request)
        )


def add_to_cart(request, decal_id, quantity):
    decal = Decal.objects.get(id=decal_id)
    cart = Cart(request)
    cart.add(decal, decal.price, quantity)


def remove_from_cart(request, decal_id):
    decal = Decal.objects.get(id=decal_id)
    cart = Cart(request)
    cart.remove(decal)