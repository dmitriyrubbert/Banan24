# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from api.models import Female, Message, User

@admin.register(Female)
class FemaleAdmin(admin.ModelAdmin):
    list_display = ('site_id','end_activation', 'end_mailactivation', 'last_update')
    # list_filter = ['country',]
    search_fields = ['site_id', ]
    # filter_horizontal = ('template',)
    # exclude = ['added_by',]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('woman_id','man_id', 'display_text')
    # list_filter = ['country',]
    search_fields = ['woman_id', 'man_id', 'sender']
    # filter_horizontal = ('template',)
    # exclude = ['added_by',]

admin.site.register(User)