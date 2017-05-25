from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Aged
from .forms import AddForm

def index(request):
    aged = Aged.objects.filter(is_missing=True)
    context = {
        'aged': aged,
    }
    return render(request, 'missing/index.html', context)


@login_required
def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            missing = form.save(commit=False)
            missing.family = request.user
            missing.save()
            return redirect(reverse('index'))
    else:
        form = AddForm()

    context = {
        'form': form,
    }
    return render(request, 'missing/add.html', context)
