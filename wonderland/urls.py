from django.urls import path
from wonderland import views
app_name = 'wonderland'
urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),

]