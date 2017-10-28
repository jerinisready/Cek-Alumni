# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Cekian, Post, Comment

# Register your models here.
admin.site.register(Cekian)


class ChoiceInline(admin.TabularInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,       {'fields': ['text', 'image', 'like', 'user', 'deleted']}),
        # ('Comments', {'fields': ['text', 'like', 'user', 'deleted'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    class meta:
        model = Post


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

