# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class UpdatesConfig(AppConfig):
    name = 'updates'

    def ready(self):
        from updates.models import print_all_field_changes
        from fieldsignals import pre_save_changed
        from updates.models import Instance
        pre_save_changed.connect(print_all_field_changes, sender=Instance)