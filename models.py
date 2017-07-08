# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Recalls(models.Model):
    record_id = models.IntegerField(db_column='RECORD_ID')  # Field name made lowercase.
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

    class Meta:
        managed = False
        db_table = 'recalls'
