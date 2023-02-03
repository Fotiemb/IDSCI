from django.urls import path
from .views import HomeView, loginPage, profile, message, reserver

app_name = "librairie"
urlpatterns = [
    path('dashboard/', HomeView.as_view(), name='pageHome'),
    path('profile/', profile, name='dashProfile'),
    path('message/', message, name='message'),
    path('aide/', message, name='aide'),
    path('reserver/', reserver, name='reserver'),

]
