from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Use the name of the view function, not the template
]
