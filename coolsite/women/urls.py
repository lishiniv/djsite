from django.urls import path, re_path, register_converter

from . import converters
from .views import *

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', index, name='home'),
    path('cats/<int:cat_id>/', cats, name='cats'),
    path('cats/<slug:cat_slug>/', categories, name='categories'),
    path('archive/<year4:year>/', archive, name='archive'),
]
