from django.contrib import admin
from django.conf.urls import url
from django.shortcuts import render
from django.contrib.admin import helpers
from db.models import *
from db.forms import (
    UserFactorItemsForm,
    UserFactorForm,
    RestaurantReportForm,
    CustomerReportForm,
    CustomSQLForm
)

# Register your models here.

def get_all_fields(clls):
    return [field.name for field in clls._meta.get_fields()]
    

class AddressAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "phone", "user"]

class AddressLogAdmin(admin.ModelAdmin):
    list_display = get_all_fields(AddressLog)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["ssn", "name", "surname", "phone", "age"]
    change_list_template = 'change_list_customer.html'
    resturant_export_template = "restaurant_report.html"
    customer_export_template = "customer_report.html"

    def get_urls(self):
        urls = super(CustomerAdmin, self).get_urls()
        custom_urls = [
            url(r'export_restaurant_report/$',
            self.admin_site.admin_view(self.export_restaurant_report),
            name='db_export_restaurant_report'),
            url(r'export_customer_report/$',
            self.admin_site.admin_view(self.export_customer_report),
            name='db_export_customer_report')
        ]
        return custom_urls + urls

    def export_restaurant_report(self, request):
        context = {
            'title': ("Export Restaurant Report"),
            'app_label': self.model._meta.app_label,
            'opts': self.model._meta,
            'has_change_permission': self.has_change_permission(request)
        }
        if request.method == 'POST':
            export_form = RestaurantReportForm(request.POST)
            if export_form.is_valid():
                return export_form.save()
        else:
            export_form = RestaurantReportForm()
        context['form'] = export_form
        context['adminform'] = helpers.AdminForm(export_form,
                                                    list([(None, {'fields': export_form.base_fields})]),
                                                    {})
        return render(request, self.resturant_export_template, context)

    def export_customer_report(self, request):
        context = {
            'title': ("Export Customer Report"),
            'app_label': self.model._meta.app_label,
            'opts': self.model._meta,
            'has_change_permission': self.has_change_permission(request)
        }
        if request.method == 'POST':
            export_form = CustomerReportForm(request.POST)
            if export_form.is_valid():
                return export_form.save()
        else:
            export_form = CustomerReportForm()
        context['form'] = export_form
        context['adminform'] = helpers.AdminForm(export_form,
                                                    list([(None, {'fields': export_form.base_fields})]),
                                                    {})
        return render(request, self.customer_export_template, context)
            
    
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
    change_list_template = 'change_list_logs.html'
    custom_sql_template = "custom_sql_query.html"

    def get_urls(self):
        urls = super(LogAdmin, self).get_urls()
        custom_urls = [
            url(r'custom_sql_query/$',
            self.admin_site.admin_view(self.custom_sql_render),
            name='db_custom_sql_query'),
        ]
        return custom_urls + urls

    def custom_sql_render(self, request):
        context = {
            'title': ("Run your sql query"),
            'app_label': self.model._meta.app_label,
            'opts': self.model._meta,
            'has_change_permission': self.has_change_permission(request)
        }
        if request.method == 'POST':
            export_form = CustomSQLForm(request.POST)
            if export_form.is_valid():
                return export_form.save()
        else:
            export_form = CustomSQLForm()
        context['form'] = export_form
        context['adminform'] = helpers.AdminForm(export_form,
                                                    list([(None, {'fields': export_form.base_fields})]),
                                                    {})
        return render(request, self.custom_sql_template, context)

class ShoppingFactorAdmin(admin.ModelAdmin):
    list_display = get_all_fields(ShoppingFactor)

class ShoppingFactorLogsAdmin(admin.ModelAdmin):
    list_display = get_all_fields(ShoppingFactorLog)

class StoreAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active"]

class StoreLogAdmin(admin.ModelAdmin):
    list_display = get_all_fields(StoreLog)

class UserFactorAdmin(admin.ModelAdmin):
    list_display = ["__str__", "delivery", "total_price", "date"]

    def user(self, obj):
        return obj.user.ssn
    
    form = UserFactorForm

class UserFactorLogAdmin(admin.ModelAdmin):
    list_display = get_all_fields(UserFactorsLog)

class UserFactorsItemAdmin(admin.ModelAdmin):
    list_display = get_all_fields(UserFactorsItem)

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


""" 
    def get_queryset(self, request):
        return AddressLog.objects.all().union(
            CustomerLog.objects.all(),
            DeliveryLog.objects.all(),
            MenuFoodLog.objects.all(),
            ShoppingFactorLog.objects.all(),
            StoreLog.objects.all(),
            UserFactorsLog.objects.all(),
            UserFactorsItemsLog.objects.all()
        ) """

