# ex02/forms.py

from django import forms

class EntryForm(forms.Form):
    text = forms.CharField(label='Text', max_length=100)