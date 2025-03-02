from django import forms
from .models import watched_series, watched_later_series

class watch_form(forms.ModelForm):
    class Meta:
      model = watched_series
      fields=['name','image']

class later_form(forms.ModelForm):
    class Meta:
        model=watched_later_series
        fields=['name','image']
