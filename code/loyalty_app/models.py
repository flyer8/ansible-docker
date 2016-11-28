# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Permissions(models.Model):
    permissionid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class Userpermissions(models.Model):
    userpermissionid = models.AutoField(primary_key=True)
    userid = models.IntegerField(blank=True, null=True)
    permissionid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userpermissions'


class Users(models.Model):
    userid = models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=40, blank=True, null=True)
    login = models.CharField(max_length=20, blank=True, null=True)
    hashpassword = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
