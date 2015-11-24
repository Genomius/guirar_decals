# coding: utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from catalog.models import Decal
from models import Cart, DecalInCart, Order
from forms import DecalInCartForm


def cart(request):
    if request.session.get("cart_id", False):
        try:
            cart = Cart.objects.get(id=request.session.get("cart_id"))
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
            request.session["cart_id"] = cart.id
    else:
        cart = Cart.objects.create()
        request.session["cart_id"] = cart.id
    print request.session.get("decal_id")
    decal = Decal.objects.get(id=request.session.get("decal_id"))
    print decal + " " + cart
    decal_in_cart_form = DecalInCartForm(cart=cart, decal=decal, quantity=1)
    decal_in_cart_form.save()
    if request.method == 'POST':
        if request.is_ajax():
            if request.session.get("cart_id", False):
                try:
                    cart = Cart.objects.get(id=request.session.get("cart_id"))
                except Cart.DoesNotExist:
                    cart = Cart.objects.create()
                    request.session["cart_id"] = cart.id
            else:
                cart = Cart.objects.create()
                request.session["cart_id"] = cart.id

            decal = Decal.objects.get(id=request.session.get("decal_id"))
            print decal + " " + cart
            decal_in_cart_form = DecalInCartForm(cart=cart, decal=decal, quantity=1)
            decal_in_cart_form.save()
        else:
            pass
    else:
        return render_to_response(
            'cart.html',
            {
                '': '',
            },
            context_instance=RequestContext(request)
        )