# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from updates.models import Instance
from updates.ec2_tools import EC2
from updates.response import JSONResponse, response_mimetype

ec2 = EC2()

def home(request):
    instances = Instance.objects.all()
    return render(request, 'main.html', {'instances': instances})

def refresh_instances(request):
    updated_instances = ec2.update_db()
    return JSONResponse(updated_instances, mimetype=response_mimetype(request))