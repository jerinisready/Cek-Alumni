# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Cekian(AbstractUser):
    passout = models.IntegerField(null=True, validators=[MaxValueValidator(int(time.strftime("%Y")),
                                                                MinValueValidator(1980))])
    bio = models.TextField(null=True)
    address = models.TextField(null=True, blank=True)
    office = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True)
    working_as = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.CharField(max_length=1024, null=True, blank=True)





