from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addflavor", views.add_flavor, name="addflavor"),
    path('delete/<int:pk>/', views.delete_flavor, name='deleteflavor'),
    path('edit/<int:pk>/', views.edit_flavor, name='editflavor'),
]