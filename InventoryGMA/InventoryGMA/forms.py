from django import forms

from .models import Category, Thing

class ThingForm(forms.ModelForm):
    #name = forms.CharField(label="Thing's name", min_length=2, max_length=100, initial="", required=True)
    #description = forms.CharField(label="Description", max_length=100, initial="", required=False)
    #category = forms.ModelChoiceField(queryset=Category.objects.all(), to_field_name="name", required=False)
    #quantity = forms.IntegerField(label="Quantity of things", max_value=100, min_value=1, initial=1, required=True)
    class Meta:
        model = Thing
        fields = ["name", "description", "category", "quantity"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = [] #Include all fields