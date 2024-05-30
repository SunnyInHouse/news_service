"""URLs configuration of the endpoints 'news' of the 'Api' application v1."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.news.views import NewsViewSet

router_v1 = DefaultRouter()

router_v1.register("", NewsViewSet, basename="news")

urlpatterns = [path("", include(router_v1.urls))]
