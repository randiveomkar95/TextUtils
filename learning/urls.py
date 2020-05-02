from django.urls import path
from .views import home, one_to_many, export_csv, export_data

app_name='learning'

urlpatterns = [
     path('', home, name='index'),
     path('one_to_many/', one_to_many, name='one_to_many'),
     path('export/', export_csv, name='export_csv'),
     path('export-data/', export_data, name='export_data'),
]
