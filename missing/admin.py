from django.contrib import admin

from .models import Person, Witness

class WitnessInline(admin.StackedInline):
    model = Witness
    extra = 3

class PersonAdmin(admin.ModelAdmin):
    inlines = [WitnessInline]

admin.site.register(Person, PersonAdmin)
