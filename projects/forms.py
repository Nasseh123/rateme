from django import forms
from .models import Profile,webapps,ratings

class profileform(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user','pub_date']
    
class webappsform(forms.ModelForm):
    class Meta:
        model=webapps
        exclude=['profile','user','pub_date']

class ratingsform(forms.ModelForm):
    class Meta:
        model=ratings
        exclude=['webapp','user']