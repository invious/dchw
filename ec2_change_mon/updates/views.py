# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def ec2_(request, emp_id):
	employee = Employee.objects.get(id=emp_id)
	assets = Asset.objects.filter(owned_by=employee)

	return render(request, 'owned_assets_table.html', {'assets': assets})
