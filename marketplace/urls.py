from django.urls import path

from . import views

app_name = "marketplace"
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /marketplace/johnsmith/
    path('<str:username>/', views.profile, name='profile'),
    # ex: /marketplace/johnsmith/gallery/
    path('<str:username>/gallery/', views.gallery, name='gallery'),
    # ex: /marketplace/johnsmith/uploadArt/
    path('<str:username>/create/', views.create, name='create'),
]