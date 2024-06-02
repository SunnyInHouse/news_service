"""URLs configuration of the 'Api' application."""

from django.urls import include, path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

app_name = "api"

urlpatterns = [
    path("v1/", include("api.v1.urls")),
    path(
        "doc/download/v1/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        "doc/swagger/v1/",
        SpectacularSwaggerView.as_view(url_name="api:schema"),
        name="swagger",
    ),
]
