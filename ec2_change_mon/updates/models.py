# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Instance(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    contract = models.CharField(max_length=128)
    terminated = models.BooleanField(default=False)
