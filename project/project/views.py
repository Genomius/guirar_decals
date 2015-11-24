# coding: utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from catalog.models import Decal


def home(request):
    decals = Decal.objects.all()

    return render_to_response(
        'home.html',
        {
            'decals': decals,
        },
        context_instance=RequestContext(request)
    )