from django import forms
from django.forms import ModelForm
from . models import *

class Meta:
    model = Booking
    fields = ('checkin','checkout')
