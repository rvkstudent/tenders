# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tenders(models.Model):
    tender_id = models.TextField(primary_key=True)
    auction_type = models.TextField(blank=True, null=True)
    zakup_status = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    date_modified = models.DateField(blank=True, null=True)
    organisation = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_found = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenders'

class Words(models.Model):
    
    phrase = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'words'


class TendersStat(models.Model):
    last_update = models.TextField(blank=True, null=True)
    last_launch = models.TextField(blank=True, null=True)
    before = models.TextField(blank=True, null=True)
    after = models.TextField(blank=True, null=True)
    change = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tenders_stat'


class TendersTsc(models.Model):
    tender_id = models.TextField(primary_key=True)
    auction_type = models.TextField(blank=True, null=True)
    zakup_status = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    date_modified = models.DateField(blank=True, null=True)
    organisation = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_found = models.DateTimeField(blank=True, null=True)
    manager = models.TextField(blank=True, null=True)
    phrase = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenders_tsc'

