from tabnanny import verbose
from django.db import models

# Create your models here.

class Mother(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Child(models.Model):
    name = models.CharField(max_length=20)
    dob = models.DateField()
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'children'

class Deposit(models.Model):
    amount = models.IntegerField(default=0)
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE)
    deposit_date = models.DateField()

    def __str__(self):
        return self.mother.name

#class Policy