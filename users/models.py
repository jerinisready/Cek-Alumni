# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Cekian(AbstractUser):
    bio = models.TextField(null=True)
    address = models.TextField(null=True, blank=True)
    office = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True)
    working_as = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.CharField(max_length=1024, null=True, blank=True)
    birth_day = models.DateField(blank=True, null=True)
    wed_day = models.DateField(blank=True, null=True)
    gender = models.CharField(null=True, max_length=10, choices=(('Mr', 'Male'), ('Mrs', 'Female')))
    passout = models.IntegerField(null=True, validators=[MaxValueValidator(int(time.strftime("%Y")),
                                                                           MinValueValidator(1980))])

    def __str__(self):
        return self.first_name + " ( @" + self.username + " )"


class Post(models.Model):
    text = models.TextField()
    image = models.ImageField()
    deleted = models.BooleanField(default=False)
    user = models.ForeignKey('Cekian', on_delete=models.CASCADE, )
    datetime = models.DateTimeField(auto_now_add=datetime.now(), blank=True, null=True)
    like = models.ManyToManyField(Cekian, related_name='post_liked_ones')

    def __str__(self):
        return self.text

    def liked_by(self, user):
        return self.like.get(pk=user.id).exists()

    def likes(self):
        return self.like.count()

    def comments(self):
        return self.comments_set.count()


class Comment(models.Model):
    text = models.TextField()
    like = models.ManyToManyField(Cekian, related_name='likes_ones')
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('Cekian', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=datetime.now(), blank=True, null=True)
    deleted = models.BooleanField()

    def __str__(self):
        return self.text

    def liked_by(self, user):
        return self.like.get(pk=user.id).exists()






