from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields

from .models import Items,Demand

class ItemsForm(forms.ModelForm):
    class Meta:
        model =Items
        fields='__all__'

#    def save(self):new_item=Items.objects.create(name=self.cleaned_data.get('name'),            price =self.cleaned_data.get('price'),)


class DemandForm(forms.ModelForm):
    class Meta:
        model =Demand
        fields='__all__'
class IssueForm(forms.ModelForm):
	class Meta:
		model = Demand
		fields = ['quantity']







#title.widget.attrs.update({'class':'form-control'})
#slug.widget.attrs.update({'class':'form-control'})

#def clean_slug(self):
#new_slug=self.cleaned_data.get('name').lower()
#if new_slug=='create':
#raise ValidationError ('slug may not be created')
#return new_slug

    