"""Viewsets for endpoints of the 'Api' application v1."""

from rest_framework import mixins, viewsets


class GetPostPutDeleteViewSet(viewsets.ModelViewSet):
    """The viewset allows methods: GET, POST, PUT, DELETE."""

    http_method_names = ("get", "post", "put", "delete", "head", "options")


class GetPostDeleteViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """The viewset allows methods: GET, POST, PUT, DELETE."""

    pass
