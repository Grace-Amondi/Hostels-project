# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.serializers import serialize
from django.http import HttpResponse

from django.shortcuts import render
from .models import Hostel


def home(request):
    return render(request, 'index.html')


def hostel_data_view(request):
    data = serialize('geojson', Hostel.objects.all())
    return HttpResponse(data, content_type='application/json')
