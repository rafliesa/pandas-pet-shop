from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm) :
    class Meta:
        model = Item
        fields = ['name','photo','price','description','animal_type','stock']