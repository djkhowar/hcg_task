from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path("validate-data/",views.validateForm, name="validate_data")
]
