# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models


class Owner(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField()

    def __unicode__(self):
        return self.name


class Hostel(models.Model):
    TYPE_CHOICES = (
        ('bedsitter', 'Bedsitter'),
        ('single', 'Single'),
    )
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, blank=True, null=True)
    location = models.PointField(srid=4326)
    owner = models.ForeignKey(Owner, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
