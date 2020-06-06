from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('site/',views.site,name='site'),
    path('profile/<username>',views.profile,name='profile'),
    path('search/',views.search_all_projects,name='search_all_projects')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)