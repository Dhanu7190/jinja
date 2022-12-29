from django.urls import path
from app1.views import *
app_name='any1'
urlpatterns=[
    path('jinja/',jinja,name='jinja'),
]