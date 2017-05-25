from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Person
from .forms import AddForm, WitnessForm

def index(request):
    context = {
        'persons': Person.objects.filter(is_missing=True),
    }
    return render(request, 'missing/index.html', context)


@login_required
def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.family = request.user
            person.save()
            return redirect(reverse('index'))
    else:
        form = AddForm()

    context = {
        'form': form,
    }
    return render(request, 'missing/add.html', context)


@login_required
def detail(request, id):
    person = get_object_or_404(Person, id=id)
    if request.method == 'POST':
        form = WitnessForm(request.POST)
        if form.is_valid():
            witness = form.save(commit=False)
            witness.target = person
            witness.user = request.user
            witness.save()
            return redirect(reverse('detail', kwargs={'id':id}))
    else:
        form = WitnessForm()

    context = {
        'person': person,
        'form': form,
    }
    return render(request, 'missing/detail.html', context)
