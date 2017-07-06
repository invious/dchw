# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from updates.models import Instance
from django.conf import settings


def home(request):
    instances = Instance.objects.all()
    return render(request, 'main.html', {'instances': instances})

def refresh_instances(request):
    pass