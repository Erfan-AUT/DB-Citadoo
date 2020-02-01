from django import forms
from datetime import date
from io import BytesIO
from django.http import FileResponse
from db.models import *
from django.utils.encoding import smart_str
from django.db.models import Count, Sum
from django.db import connection
from django.utils import timezone

class UserFactorItemsForm(forms.ModelForm):

    class Meta:
        model = UserFactorsItem
        exclude = ('price_per',)

    foodChoices = MenuFood.objects.all()

    item = forms.ModelChoiceField(queryset=foodChoices)

    def save(self, commit=True):
        instance = super(UserFactorItemsForm, self).save(commit=False)
        name, price = instance.item.split(':')
        instance.item = name
        instance.price_per = price
        instance.save()
        related_factor = UserFactor.objects.get(pk=instance.factor_id)
        related_factor.total_price += int(price) * instance.count
        related_factor.save()

        return instance

class UserFactorForm(forms.ModelForm):

    class Meta:
        model = UserFactor
        exclude = ('total_price',)


    def save(self, commit=True):
        
        instance = super(UserFactorForm, self).save(commit=False)        
        if instance.user and (instance.address.user_id != instance.user.pk or not instance.delivery):
            raise forms.ValidationError("Address doesnt belong to user!")
        instance.save()
        return instance


def create_file_response(file_str, title):
    file_bytes = str.encode(file_str, encoding='utf-8')
    file_IOBytes = BytesIO(file_bytes)
    response = FileResponse(file_IOBytes)
    response['Content-Disposition'] = 'attachment; filename= {}'.format(smart_str(title))
    return response 

    

class RestaurantReportForm(forms.Form):

    # For today!
    def save(self):
        today = date.today()
        user_factors = list(UserFactor.objects.filter(date__date=today))
        shopping_factors = list(ShoppingFactor.objects.filter(date__date=today))
        user_buys = [factor.total_price for factor in user_factors]
        store_buys = [factor.price for factor in shopping_factors]
        sum_user_buys = sum(user_buys)
        sum_store_buys = sum(store_buys)
        product = sum_user_buys - sum_store_buys
        file_str = """
            List of today's sells to users is: {} \n
            List of today's buys from stores is: {} \n
            Sum of today's sells is: {} \n
            Sum of today's buys is: {} \n
            Today's product is: {}
        """
        file_str = file_str.format(str(user_buys), str(store_buys), str(sum_user_buys), str(sum_store_buys), str(product))
        return create_file_response(file_str, "Restaurantsreport.txt")
        


class CustomerReportForm(forms.Form):

    users = Customer.objects.all()
    customer = forms.ModelChoiceField(queryset=users, required=True)

    def save(self):
        currentCustomer = self.cleaned_data['customer']
        currentCustomerSSN = currentCustomer.ssn
        currentCustomerID = currentCustomer.pk
        customerFactorItems = UserFactorsItem.objects.filter(factor__user=currentCustomerID)
        fav_food = customerFactorItems.values('item').annotate(c=Count('item')).order_by('-item').first()['item']
        #fav_food = customerFactorItems.objects.values('item').annotate(c=Count('item')).order_by('-item').first()
        customerFactors = UserFactor.objects.filter(user=currentCustomerID)
        sum_buys = customerFactors.aggregate(Sum('total_price'))['total_price__sum']
        file_str = """
            Customer with SSN {} 's favorite food is: {} \n
            And the sum of his/her buys is: {}
        """
        file_str = file_str.format(currentCustomerSSN, fav_food, str(sum_buys))
        return create_file_response(file_str, "Customer{}sReport.txt".format(currentCustomerSSN))


class CustomSQLForm(forms.Form):
    
    query = forms.CharField(widget=forms.Textarea)

    def save(self):
        query_text = self.cleaned_data['query']
        with connection.cursor() as cursor:
            cursor.execute(query_text)
            columns = [col[0] for col in cursor.description]
            final_result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            result_str = str(final_result)
            return create_file_response(result_str, "QueryResult.txt")

            



