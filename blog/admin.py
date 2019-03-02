# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

admin.site.register(models.Tenders)
admin.site.register(models.Words)
admin.site.register(models.TendersTsc)

# Register your models here.
