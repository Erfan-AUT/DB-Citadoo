# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from db.utils import create_proper_log, none_to_empty

class Address(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    user = models.ForeignKey('Customer', models.CASCADE, db_column='user')

    class Meta:
        verbose_name_plural = "addresses"
        db_table = 'address'
    
    def __str__(self):
        return str(self.user) + ": " + self.name
    
    def save(self, *args, **kwargs):
        is_created = True
        if self.pk:
            is_created = False
        self_str = str(self)
        super(Address, self).save(*args, **kwargs)
        if is_created: 
            create_proper_log(AddressLog, self_str, "Insert")
        else:
            create_proper_log(AddressLog, self_str, "Update")
    
    def delete(self):
        self_str = str(self)
        super(Address, self).delete()
        create_proper_log(AddressLog, self_str, "Delete")

    

class AddressLog(models.Model):
    id = models.AutoField(primary_key=True)
    changed_data = models.CharField(max_length=255)
    changed_date = models.DateTimeField(null=False)
    change_type =  models.CharField(max_length=255)

    class Meta:
        db_table = 'address_log'


class Customer(models.Model):
    ssn = models.CharField(unique=True, max_length=255, null=False)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    age = models.IntegerField()

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return str(self.ssn) + " " + self.name + " " + self.surname
    
    def save(self, *args, **kwargs):
        is_created = True
        if self.pk:
            is_created = False
        self_str = str(self)
        super(Customer, self).save(*args, **kwargs)
        if is_created: 
            create_proper_log(CustomerLog, self_str, "Insert")
        else:
            create_proper_log(CustomerLog, self_str, "Update")
    
    def delete(self):
        self_str = str(self)
        super(Customer, self).delete()
        create_proper_log(CustomerLog, self_str, "Delete")


class CustomerLog(models.Model):
    id = models.AutoField(primary_key=True)
    changed_data = models.CharField(max_length=255)
    changed_date = models.DateTimeField(null=False)
    change_type =  models.CharField(max_length=255)

    class Meta:
        
        db_table = 'customer_log'


class Delivery(models.Model):
    ssn = models.CharField(unique=True, max_length=255, null=False)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'delivery'
    
    def __str__(self):
        return self.name + " " + self.surname
    
    def save(self, *args, **kwargs):
        is_created = True
        if self.pk:
            is_created = False
        self_str = str(self)
        super(Delivery, self).save(*args, **kwargs)
        if is_created: 
            create_proper_log(DeliveryLog, self_str, "Insert")
        else:
            create_proper_log(DeliveryLog, self_str, "Update")
    def delete(self):
        self_str = str(self)
        super(Delivery, self).delete()
        create_proper_log(DeliveryLog, self_str, "Delete")


class DeliveryLog(models.Model):
    id = models.AutoField(primary_key=True)
    changed_data = models.CharField(max_length=255)
    changed_date = models.DateTimeField(null=False)
    change_type =  models.CharField(max_length=255)

    class Meta:
        db_table = 'delivery_log'


class Log(models.Model):
    changed_data = models.CharField(max_length=255)
    changed_date = models.DateTimeField(null=False)
    change_type =  models.CharField(max_length=255)

    class Meta:
        db_table = 'log'


class MenuFood(models.Model):
    name = models.CharField(unique=True, max_length=255, null=False)
    price = models.IntegerField(null=False)

    class Meta:
        db_table = 'menu_food'
    
    def __str__(self):
        return self.name + ": " + str(self.price)
    
    def save(self, *args, **kwargs):
        is_created = True
        if self.pk:
            is_created = False
        self_str = str(self)
        super(MenuFood, self).save(*args, **kwargs)
        if is_created: 
            create_proper_log(MenuFoodLog, self_str, "Insert")
        else:
            create_proper_log(MenuFoodLog, self_str, "Update")

    def delete(self):
        self_str = str(self)
        super(MenuFood, self).delete()
        create_proper_log(MenuFoodLog, self_str, "Delete")



class MenuFoodLog(models.Model):
    id = models.AutoField(primary_key=True)
    changed_data = models.CharField(max_length=255)
    changed_date = models.DateTimeField(null=False)
    change_type =  models.CharField(max_length=255)

    class Meta:
        db_table = 'menu_food_log'
    


class ShoppingFactor(models.Model):
    id = models.IntegerField(primary_key=True)
    store = models.ForeignKey('Store', models.DO_NOTHING, db_column='store', null=False)
    item = models.CharField(max_length=255)
    price = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        db_table = 'shopping_factor'
    
    def save(self, *args, **kwargs):
        is_created = True
        if self.pk:
            is_created = False
        self_str = str(self)
        super(ShoppingFactor, self).save(*args, **kwargs)
        if is_created: 
            create_proper_log(ShoppingFactorLog, self_str, "Insert")
        else:
            create_proper_log(ShoppingFactorLog, self_str, "Update")
    
    def delete(self):
        self_str = str(self)
        super(ShoppingFactor, self).delete()
        create_proper_log(ShoppingFactorLog, self_str, "Delete")


class ShoppingFactorLog(models.Model):
    id = models.AutoField(primary_key=True)
    changed_data = models.CharField(max_length=255)
    changed_date = models.DateTimeField(null=False)
    change_type =  models.CharField(max_length=255)

    class Meta:
        db_table = 'shopping_factor_log'


class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, null=False)
    is_active = models.BooleanField(null=False, default=True)

    class Meta:
        db_table = 'store'

    def delete(self):
        self_str = str(self)
        self.is_active = False
        self.save()
        create_proper_log(StoreLog, self_str, "Delete")
    
    def save(self, *args, **kwargs):
        is_created = True
        if self.pk:
            is_created = False
        self_str = str(self)
        super(Store, self).save(*args, **kwargs)
        if is_created: 
            create_proper_log(StoreLog, self_str, "Insert")
        else:
            create_proper_log(StoreLog, self_str, "Update")



class StoreLog(models.Model):
    id = models.AutoField(primary_key=True)
    changed_data = models.CharField(max_length=255)
    changed_date = models.DateTimeField(null=False)
    change_type =  models.CharField(max_length=255)

    class Meta:
        db_table = 'store_log'


class UserFactor(models.Model):
    user = models.ForeignKey(Customer, models.DO_NOTHING, db_column='user', blank=True, null=True)
    address = models.ForeignKey(Address, models.SET_NULL, db_column='address', blank=True, null=True)
    delivery = models.ForeignKey(Delivery, models.SET_NULL, db_column='delivery', blank=True, null=True)
    total_price = models.IntegerField(null=False, default=0)
    date = models.DateTimeField(null=False)

    class Meta:
        db_table = 'user_factor'
    
    def __str__(self):
        return str(self.id) + " " +  none_to_empty(str(self.user)) + " " + none_to_empty(str(self.address))
    
    def save(self, *args, **kwargs):
        is_created = True
        if self.pk:
            is_created = False
        self_str = str(self)
        super(UserFactor, self).save(*args, **kwargs)
        if is_created: 
            create_proper_log(UserFactor, self_str, "Insert")
        else:
            create_proper_log(UserFactor, self_str, "Update")
    
    def delete(self):
        self_str = str(self)
        super(UserFactor, self).delete()
        create_proper_log(UserFactorsLog, self_str, "Delete")


class UserFactorsLog(models.Model):
    id = models.AutoField(primary_key=True)
    changed_data = models.CharField(max_length=255)
    change_type =  models.CharField(max_length=255)
    changed_date = models.DateTimeField(null=False)

    class Meta:
        db_table = 'user_factors_log'



class UserFactorsItem(models.Model):
    id = models.AutoField(primary_key=True)
    factor = models.ForeignKey(UserFactor, models.CASCADE, db_column='factor')
    item = models.CharField(max_length=255)
    price_per = models.IntegerField(null=False)
    count = models.IntegerField(null=False)

    class Meta:
        db_table = 'user_factors_item'
        unique_together = (('factor', 'item'),)
    
    def save(self, *args, **kwargs):
        is_created = True
        if self.pk:
            is_created = False
        self_str = str(self)
        super(UserFactorsItem, self).save(*args, **kwargs)
        if is_created: 
            create_proper_log(UserFactorsItemLog, self_str, "Insert")
        else:
            create_proper_log(UserFactorsLog, self_str, "Update")
    
    def delete(self):
        self_str = str(self)
        super(UserFactorsItem, self).delete()
        create_proper_log(UserFactorsItemsLog, self_str, "Delete")


class UserFactorsItemsLog(models.Model):
    id = models.AutoField(primary_key=True)
    changed_data = models.CharField(max_length=255)
    changed_date = models.DateTimeField(null=False)
    change_type =  models.CharField(max_length=255)

    class Meta:
        db_table = 'user_factors_items_log'
