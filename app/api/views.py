import traceback

from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED, HTTP_404_NOT_FOUND

import api.models as models
from api.serializers import SignUpSerializer, FavoritesSerializer


class AccessTokenParameter(openapi.Parameter):
    def __init__(self,**extra):
        super().__init__(
            name='Authorization',
            in_='header',
            required=True,
            type=openapi.TYPE_STRING,
            description="Session JWT",
            format="Bearer ACCESS-JWT",
            **extra
        )


class SignUp(CreateAPIView):
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        headers = self.get_success_headers(serializer.data)

        return Response(data, status=HTTP_201_CREATED, headers=headers)


@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        manual_parameters=[AccessTokenParameter()],
        operation_description="Listado de Cómics Favoritos"
    )
)
@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        manual_parameters=[AccessTokenParameter()],
        operation_description="Registrar Cómic Favorito"
    )
)
class FavoritesCR(ListAPIView, CreateAPIView):
    serializer_class = FavoritesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Favorites.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@method_decorator(
    name="delete",
    decorator=swagger_auto_schema(
        manual_parameters=[AccessTokenParameter()],
        operation_description="Eliminar Cómic del listado de Favoritos"
    )
)
class FavoritesUD(DestroyAPIView):
    serializer_class = FavoritesSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        try:
            instance = models.Favorites.objects.get(comicId=kwargs['comicId'])
            self.perform_destroy(instance)
            return Response(status=HTTP_204_NO_CONTENT)
        except Exception as e:
            traceback.print_exc(e)
            return Response(status=HTTP_404_NOT_FOUND)

