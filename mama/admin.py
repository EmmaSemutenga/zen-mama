from django.contrib import admin

# Register your models here.
from .models import Mother, Child, Deposit

admin.site.register(Mother)
admin.site.register(Child)
admin.site.register(Deposit)