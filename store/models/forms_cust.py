from typing import ClassVar
from django import forms
from django.db import models
from django.forms import fields
from store.models.customer import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

