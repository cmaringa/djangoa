# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class IndexStatic(models.Model):
    isin = models.TextField(db_column='ISIN', blank=True, null=True)
    sedol = models.TextField(db_column='SEDOL', blank=True, null=True)
    ric = models.TextField(db_column='RIC', blank=True, null=True)
    cusip = models.FloatField(db_column='CUSIP', blank=True, null=True)
    instrument_name = models.TextField(db_column='Instrument_Name', blank=True, null=True)
    country = models.TextField(db_column='Country', blank=True, null=True)
    currency = models.TextField(db_column='Currency', blank=True, null=True)
    exchange = models.TextField(db_column='Exchange', blank=True, null=True)
    sector = models.IntegerField(db_column='Sector', blank=True, null=True)
    load_time = models.TextField(db_column='load_time', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'index_static'


class IndexTS(models.Model):
    Date = models.TextField(db_column='Date', blank=True, null=True)
    index_symbol = models.TextField(db_column='Index_Symbol', blank=True,
                                    null=True)
    isin = models.TextField(db_column='ISIN', blank=True, null=True)
    shares = models.IntegerField(db_column='Shares', blank=True, null=True)
    free_float = models.FloatField(db_column='Free_Float', blank=True, null=True)
    capfactor = models.IntegerField(db_column='Capfactor', blank=True, null=True)
    price = models.FloatField(db_column='Price', blank=True, null=True)
    load_time = models.DateTimeField(db_column='load_time', blank=True,
                                     null=True)

    class Meta:
        managed = False
        db_table = 'index_ts'
