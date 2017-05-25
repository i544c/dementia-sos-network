from django.forms import ModelForm
from .models import Person

class AddForm(ModelForm):
    class Meta:
        model = Person
        exclude = ['family']
