from django import forms
from .models import Profile,webapps

class profileform(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user','pub_date']
    
class webappsform(forms.ModelForm):
    class Meta:
        model=webapps
        exclude=['profile','user','pub_date']