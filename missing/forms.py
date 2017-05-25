from django.forms import ModelForm, Textarea
from .models import Person, Witness

class AddForm(ModelForm):
    class Meta:
        model = Person
        exclude = ['family']

class WitnessForm(ModelForm):
    class Meta:
        model = Witness
        fields = ['comment']
        widgets = {
            'comment': Textarea(),
        }
