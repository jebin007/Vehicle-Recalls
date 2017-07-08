# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from twilio.rest import Client
import os


class DjangoMigrations(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class Register(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField()
    phone_number = models.IntegerField(max_length=15)

    def __str__(self):
        return self.name



class Recalls(models.Model):
    record_id = models.IntegerField(db_column='RECORD_ID',primary_key=True)  # Field name made lowercase.
    campno = models.TextField(db_column='CAMPNO', blank=True, null=True)  # Field name made lowercase.
    maketxt = models.TextField(db_column='MAKETXT', blank=True, null=True)  # Field name made lowercase.
    modeltxt = models.TextField(db_column='MODELTXT', blank=True, null=True)  # Field name made lowercase.
    yeartxt = models.IntegerField(db_column='YEARTXT', blank=True, null=True)  # Field name made lowercase.
    mfgcampno = models.TextField(db_column='MFGCAMPNO', blank=True, null=True)  # Field name made lowercase.
    compname = models.TextField(db_column='COMPNAME', blank=True, null=True)  # Field name made lowercase.
    mfgname = models.TextField(db_column='MFGNAME', blank=True, null=True)  # Field name made lowercase.
    bgman = models.FloatField(db_column='BGMAN', blank=True, null=True)  # Field name made lowercase.
    endman = models.FloatField(db_column='ENDMAN', blank=True, null=True)  # Field name made lowercase.
    rcltypecd = models.TextField(db_column='RCLTYPECD', blank=True, null=True)  # Field name made lowercase.
    potaff = models.FloatField(db_column='POTAFF', blank=True, null=True)  # Field name made lowercase.
    odate = models.FloatField(db_column='ODATE', blank=True, null=True)  # Field name made lowercase.
    influenced = models.IntegerField(db_column='INFLUENCED', blank=True, null=True)  # Field name made lowercase.
    mfgtxt = models.TextField(db_column='MFGTXT', blank=True, null=True)  # Field name made lowercase.
    rcdate = models.FloatField(db_column='RCDATE', blank=True, null=True)  # Field name made lowercase.
    datea = models.IntegerField(db_column='DATEA', blank=True, null=True)  # Field name made lowercase.
    rpno = models.FloatField(db_column='RPNO', blank=True, null=True)  # Field name made lowercase.
    fmvss = models.TextField(db_column='FMVSS', blank=True, null=True)  # Field name made lowercase.
    desc_defect = models.TextField(db_column='DESC_DEFECT', blank=True, null=True)  # Field name made lowercase.
    conequence_defect = models.TextField(db_column='CONEQUENCE_DEFECT', blank=True, null=True)  # Field name made lowercase.
    corrective_action = models.TextField(db_column='CORRECTIVE_ACTION', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='NOTES', blank=True, null=True)  # Field name made lowercase.
    rcl_cmpt_id = models.FloatField(db_column='RCL_CMPT_ID', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.modeltxt

    class Meta:
        managed = False
        db_table = 'recalls'
@receiver(post_save, sender=Recalls)
def send_email(sender, **kwargs):
    if kwargs.get('created', False):
        subject = "Recalls database updated!!"
        message = 'Recalls Data are Updated. Please visit the website to check updated recalls for your vehicle.'
        from_email = 'Norepoly@recalls.com'
        recievers = []
        phone_numbers = []
        #send email here:
        for user in Register.objects.all():
            recievers.append(user.email)
            phone_numbers.append(user.phone_number)
        send_mail(subject, message, from_email, recievers)
        #send sms here:
        client = Client('ACb493a7250a4e8be0dfe5eb5a79f1af75',
                        '105ec00347ed0ef65086d1891b1d26c2')
        client.messages.create(to=phone_numbers,
                               from_="+1 443-960-7070",
                               body=message)
