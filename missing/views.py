from django.shortcuts import render
from django.http import HttpResponse

from .models import Aged
from .forms import AddForm

def index(request):
    aged = Aged.objects.filter(is_missing=True)
    context = {
        'aged': aged,
    }
    return render(request, 'missing/index.html', context)


def add(request):
    form = AddForm()
    context = {
        'form': form,
    }
    return render(request, 'missing/add.html', context)
