from django import forms
from django.core import validators
import re

def email_checker(value):
  pattern = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
  if not pattern.match(value):
      raise forms.ValidationError('invalid email address')

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(validators=[email_checker])
    verify_email = forms.EmailField(label='Please verify your email')
    text = forms.CharField(widget=forms.Textarea)


    def clean(self):
        all_clean_data = super().clean()
        mail = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if mail != vmail:
            raise forms.ValidationError("Emails must match! ")




