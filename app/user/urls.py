"""
URL mappings for the user API.
"""
from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path("create/", views.CreateUserView.as_view(), name="create")
<<<<<<< HEAD
]
=======
]
>>>>>>> 53d0d9b2e70d1248cffcd085f12e77c153687fa3
