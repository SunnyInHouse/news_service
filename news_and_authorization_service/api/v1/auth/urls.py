"""URLs configuration of the endpoints 'auth' of the 'Api' application v1."""

from django.urls import path

from api.v1.auth.views import signin

urlpatterns = [
    path("", signin, name="signin"),
]
