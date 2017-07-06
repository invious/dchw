# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from updates.models import Instance, InstanceHistory

# Register your models here.
admin.site.register(Instance)
admin.site.register(InstanceHistory)