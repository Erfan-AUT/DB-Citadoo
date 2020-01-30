from django import forms
from db.models import MenuFood, UserFactorsItem

class UserFactorItemsForm(forms.Form):

    class Meta:
        model = UserFactorsItem

    foodChoices = MenuFood.objects.all()

    item = forms.ModelChoiceField(queryset=foodChoices)

    def save(self, commit=True):
        self.item = self.item['name']
        instance = super(UserFactorForm, self).save(commit=True)
        return instance