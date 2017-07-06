# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from updates.models import Instance


def home(request):
    instances = Instance.objects.all()
    return render(request, 'main.html', {'instances': instances})
