from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _

from .models import Person, Witness

class AddForm(ModelForm):
    class Meta:
        model = Person
        exclude = ['family']
        labels = {
            'first_name': _('姓'),
            'last_name': _('名'),
            'is_missing': _('今現在、行方不明か'),
        }

class WitnessForm(ModelForm):
    class Meta:
        model = Witness
        fields = ['comment']
        labels = {
            'comment': _('情報をお寄せ下さい'),
        }
        widgets = {
            'comment': Textarea(attrs={'class': 'form-control'}),
        }
