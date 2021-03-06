# coding: utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Decal


def catalog(request):
    decals = Decal.objects.all()

    return render_to_response(
        'catalog.html',
        {
            'decals': decals,
        },
        context_instance=RequestContext(request)
    )