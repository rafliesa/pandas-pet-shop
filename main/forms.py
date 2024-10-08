from django.forms import ModelForm
from main.models import Item
from django.utils.html import strip_tags

class ItemForm(ModelForm) :
    class Meta:
        model = Item
        fields = ['name','photo','price','description','animal_type','stock']
    
    def clean_name(self):
        name = self.cleaned_data['name']
        return strip_tags(name)

    def clean_desc(self):
        description = self.cleaned_data['description']
        return strip_tags(description)
    
    def clean_animal_type(self):
        type = self.cleaned_data["animal_type"]
        return strip_tags(type)