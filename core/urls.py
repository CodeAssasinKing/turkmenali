from django.urls import path
from .views import *

app_name = "core"


urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("services/", services, name="services")
]
