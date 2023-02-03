from django.urls import path

from accounts.views import importExcel, signup

app_name = "compte"
urlpatterns = [
    path('', signup, name='signup'),
    path('data/', importExcel, name='put-data'),
]
