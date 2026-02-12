from django import forms
from cars.models import Car, Type

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("image", "mark", "description", "type")

    

class SearchForm(forms.Form):
     search = forms.CharField(label="Search", required=False)
     type_id = forms.ModelChoiceField(queryset=Type.objects.all(), required=False)
     
    