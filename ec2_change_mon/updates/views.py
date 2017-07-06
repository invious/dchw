# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from updates.models import Instance
from updates.ec2_tools import EC2

ec2 = EC2()

def home(request):
    instances = Instance.objects.all()
    return render(request, 'main.html', {'instances': instances})

def refresh_instances(request):
    ec2.update_db()
    instances = Instance.objects.all()
    return render(request, 'main.html', {'instances': instances})