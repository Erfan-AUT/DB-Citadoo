from django.contrib import admin
from db.models import *
from db.forms import UserFactorItemsForm

# Register your models here.

def get_all_fields(clls):
    return [field.name for field in clls._meta.get_fields()]

class AddressAdmin(admin.ModelAdmin):
    list_display = get_all_fields(Address)

class AddressLogAdmin(admin.ModelAdmin):
    list_display = get_all_fields(AddressLog)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["ssn", "name", "surname", "phone", "age"]
    
class CustomerLogAdmin(admin.ModelAdmin):
    list_display = get_all_fields(CustomerLog)

class DeliveryAdmin(admin.ModelAdmin):
    list_display =  ["ssn", "name", "surname", "phone"]

class DeliveryLogAdmin(admin.ModelAdmin):
    list_display = get_all_fields(DeliveryLog)

class MenuFoodAdmin(admin.ModelAdmin):
    list_display = get_all_fields(MenuFood)

class MenuFoodLogAdmin(admin.ModelAdmin):
    list_display = get_all_fields(MenuFoodLog)

class LogAdmin(admin.ModelAdmin):
    list_display = get_all_fields(Log)

    def get_queryset(self, request):
        return AddressLog.objects.all().union(
            CustomerLog.objects.all(),
            DeliveryLog.objects.all(),
            MenuFoodLog.objects.all(),
            ShoppingFactorLog.objects.all(),
            StoreLog.objects.all(),
            UserFactorsLog.objects.all(),
            UserFactorsItemsLog.objects.all()
        )

class ShoppingFactorAdmin(admin.ModelAdmin):
    list_display = get_all_fields(ShoppingFactor)

class ShoppingFactorLogsAdmin(admin.ModelAdmin):
    list_display = get_all_fields(ShoppingFactorLog)

class StoreAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active"]

class StoreLogAdmin(admin.ModelAdmin):
    list_display = get_all_fields(StoreLog)

class UserFactorAdmin(admin.ModelAdmin):
    list_display = ["user", "address", "delivery", "total_price", "date"]

    def user(self, obj):
        return obj.user.ssn

class UserFactorLogAdmin(admin.ModelAdmin):
    list_display = get_all_fields(UserFactorsLog)

class UserFactorsItemAdmin(admin.ModelAdmin):
    list_display = get_all_fields(UserFactorsItem)
    class Meta:
        form = UserFactorItemsForm


class UserFactorsItemLogAdmin(admin.ModelAdmin):
    list_display = get_all_fields(UserFactorsItemsLog)


admin.site.register(Address, AddressAdmin)
admin.site.register(AddressLog, AddressLogAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerLog, CustomerLogAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(DeliveryLog, DeliveryLogAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(MenuFood, MenuFoodAdmin)
admin.site.register(MenuFoodLog, MenuFoodLogAdmin)
admin.site.register(ShoppingFactor, ShoppingFactorAdmin)
admin.site.register(ShoppingFactorLog, ShoppingFactorLogsAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(StoreLog, StoreLogAdmin)
admin.site.register(UserFactor, UserFactorAdmin)
admin.site.register(UserFactorsLog, UserFactorLogAdmin)
admin.site.register(UserFactorsItem, UserFactorsItemAdmin)
admin.site.register(UserFactorsItemsLog, UserFactorsItemLogAdmin)
