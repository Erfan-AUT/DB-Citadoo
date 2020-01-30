# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=-1)
    address = models.CharField(max_length=-1)
    phone = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'address'


class AddressLog(models.Model):
    id = models.AutoField()
    changed_data = models.CharField(max_length=-1)
    changed_table = models.CharField(max_length=-1)
    changed_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'address_log'


class Customer(models.Model):
    ssn = models.CharField(primary_key=True, max_length=-1)
    name = models.CharField(max_length=-1)
    surname = models.CharField(max_length=-1)
    phone = models.CharField(max_length=-1)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerLog(models.Model):
    id = models.AutoField()
    changed_data = models.CharField(max_length=-1)
    changed_table = models.CharField(max_length=-1)
    changed_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_log'


class Delivery(models.Model):
    ssn = models.CharField(primary_key=True, max_length=-1)
    name = models.CharField(max_length=-1)
    surname = models.CharField(max_length=-1)
    phone = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'delivery'


class DeliveryLog(models.Model):
    id = models.AutoField()
    changed_data = models.CharField(max_length=-1)
    changed_table = models.CharField(max_length=-1)
    changed_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'delivery_log'


class Log(models.Model):
    changed_data = models.CharField(max_length=-1)
    changed_table = models.CharField(max_length=-1)
    changed_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'log'


class MenuFood(models.Model):
    name = models.CharField(primary_key=True, max_length=-1)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_food'


class MenuFoodLog(models.Model):
    id = models.AutoField()
    changed_data = models.CharField(max_length=-1)
    changed_table = models.CharField(max_length=-1)
    changed_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'menu_food_log'


class ShoppingFactor(models.Model):
    id = models.IntegerField(primary_key=True)
    store = models.ForeignKey('Store', models.DO_NOTHING, db_column='store', blank=True, null=True)
    item = models.CharField(max_length=-1)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shopping_factor'


class ShoppingFactorLog(models.Model):
    id = models.AutoField()
    changed_data = models.CharField(max_length=-1)
    changed_table = models.CharField(max_length=-1)
    changed_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'shopping_factor_log'


class Store(models.Model):
    name = models.CharField(primary_key=True, max_length=-1)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store'


class StoreLog(models.Model):
    id = models.AutoField()
    changed_data = models.CharField(max_length=-1)
    changed_table = models.CharField(max_length=-1)
    changed_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'store_log'


class UserFactor(models.Model):
    user = models.ForeignKey(Customer, models.DO_NOTHING, db_column='user', blank=True, null=True)
    address = models.CharField(max_length=-1, blank=True, null=True)
    delivery = models.ForeignKey(Delivery, models.DO_NOTHING, db_column='delivery', blank=True, null=True)
    total_price = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_factor'


class UserFactorsItem(models.Model):
    factor = models.ForeignKey(UserFactor, models.DO_NOTHING, db_column='factor', blank=True, null=True)
    item = models.CharField(max_length=-1)
    price_per = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_factors_item'


class UserFactorsItemsLog(models.Model):
    id = models.AutoField()
    changed_data = models.CharField(max_length=-1)
    changed_table = models.CharField(max_length=-1)
    changed_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_factors_items_log'


class UserFactorsLog(models.Model):
    id = models.AutoField()
    changed_data = models.CharField(max_length=-1)
    changed_table = models.CharField(max_length=-1)
    changed_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_factors_log'
