from django.forms import ModelForm
from .models import Aged

class AddForm(ModelForm):
    class Meta:
        model = Aged
        exclude = ['family']
