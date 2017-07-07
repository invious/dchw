# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Instance(models.Model):
    name = models.CharField(max_length=255)
    id = models.CharField(primary_key=True, max_length=255)
    type = models.CharField(max_length=15)
    ip_address = models.CharField(max_length=15, null=True)
    state_code = models.CharField(max_length=3)
    architecture = models.CharField(max_length=15)
    monitored = models.BooleanField()
    launched = models.DateTimeField()
    placement = models.CharField(max_length=15)
    private_dns = models.CharField(max_length=63)
    public_dns = models.CharField(max_length=63)

    def __str__(self):
        return str(self.public_dns)


class InstanceHistory(models.Model):
    date = models.DateField(auto_now_add=True, blank=True)
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    changes = models.CharField(max_length=1023)


def print_all_field_changes(sender, instance, changed_fields=None, **kwargs):
    changes = ''
    for field, (old, new) in changed_fields.items():
        if old != new:
            new_change = "%s changed from %s to %s" % (field.name, old, new)
            changes = changes + '\n' + new_change

    if changes:
        InstanceHistory.objects.create(
            instance=instance, changes=changes)
