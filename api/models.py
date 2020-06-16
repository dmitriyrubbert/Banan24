# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid
from django.conf import settings

class UserAccountManager(BaseUserManager):
    use_in_migrations = True
 
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email address must be provided')
 
        if not password:
            raise ValueError('Password must be provided')
 
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)
 
    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
 
        return self._create_user(email, password, **extra_fields)
 
class User(AbstractBaseUser, PermissionsMixin):
 
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
 
    objects = UserAccountManager()
 
    email                   = models.EmailField('email', unique=True, blank=False, null=False)
    full_name               = models.CharField('full name', blank=True, null=True, max_length=400)
    # is_verified               = models.BooleanField('verified', default=False) # Add the `is_verified` flag
    # verification_uuid         = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)
    role                    = models.CharField('Роль', max_length=220, default="Translator")
    agency_id               = models.IntegerField('ID агенства', null=True, blank=True)
    last_active             = models.DateTimeField('last active', auto_now_add=True)
    is_parthner             = models.BooleanField('parthner status', default=False)
    is_staff                = models.BooleanField('staff status', default=False)
    is_active               = models.BooleanField('active', default=True)
 
    def get_short_name(self):
        return self.email
 
    def get_full_name(self):
        return self.email
 
    def __unicode__(self):
        return self.email

    class Meta:
        ordering = ('last_active',)

class Female(models.Model):
    added_by                = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE, verbose_name='Translator')
    site_id                 = models.CharField('Charming login', max_length=220)
    site_password           = models.CharField('Charming password', max_length=220)
    end_activation          = models.DateTimeField(null=True, blank=True)
    end_mailactivation      = models.DateTimeField(null=True, blank=True)
    last_update             = models.CharField('Last visit', max_length=220, null=True, blank=True)

    def __unicode__(self):
        return self.site_id

    class Meta:
        ordering = ('last_update',)

class Message(models.Model):
    sender                  = models.ForeignKey(Female, on_delete=models.CASCADE, verbose_name='Translator')
    woman_id                = models.CharField(max_length=220, blank=True, null=True)
    man_id                  = models.CharField(max_length=220, blank=True, null=True)
    message_id              = models.CharField(max_length=220, blank=True, null=True)
    last_update             = models.CharField(max_length=220, blank=True, null=True)
    text                 = models.TextField()

    def __unicode__(self):
        return self.woman_id

    class Meta:
        ordering = ('last_update',)

    def display_text(self):
            return '{} ...'.format(self.text[0:75])
    display_text.short_description = 'text'

# https://habr.com/post/160123/