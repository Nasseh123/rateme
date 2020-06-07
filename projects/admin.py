from django.contrib import admin
from .models import Profile,webapps,ratings

# Register your models here.
admin.site.register(Profile)
admin.site.register(webapps)
admin.site.register(ratings)