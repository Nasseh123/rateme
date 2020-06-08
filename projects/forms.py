from django import forms
from .models import Profile,webapps,ratings,comment

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
    
class commentform(forms.ModelForm):
    class Meta:
        model=comment
        exclude=['webapp','user']