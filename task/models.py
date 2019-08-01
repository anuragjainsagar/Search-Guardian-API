# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
#from rest_framework.authtoken.models import Token
from django.db import models

# Create your models here.
class GuardianRestAPI(models.Model):
    sectionName = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    webTitle = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.sectionName, self.webTitle)

#for user in User.objects.all():
#   Token.objects.get_or_create(user=user)