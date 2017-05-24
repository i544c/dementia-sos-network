from django.forms import ModelForm
from .models import Aged

class AddForm(ModelForm):
    class Meta:
        model = Aged
        fields = ['first_name', 'last_name', 'is_missing']
