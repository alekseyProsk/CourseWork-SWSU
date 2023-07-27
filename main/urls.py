
from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name='mainPage'),
    path('about', views.about, name='contactInfo'),
    path('creator', views.creator, name='creatorAppeals')
]
