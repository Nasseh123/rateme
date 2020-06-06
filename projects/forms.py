from django import forms
from .models import Profile

class profileform(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user','pub_date']