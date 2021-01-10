"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.views import *

schema_view = get_schema_view(
    openapi.Info(
        title="MarvelFavs API",
        default_version='v1.0',
        description="Simple API to manage marvel favourites",
        terms_of_service="#",
        contact=openapi.Contact(email="giraldo.santiago@correounivalle.edu.co"),
        license=openapi.License(name="MIT License"),
    ),
    url=settings.API_URL,
    public=True,
)

urlpatterns = [
    # path('admin/', admin.site.urls),
    # AUTHENTICATION
    path('auth/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('auth/verify/', TokenVerifyView.as_view()),

    # Sign up
    path('auth/signup/', SignUp.as_view()),

    # Favourite Comics
    path('favorites/', FavoritesCR.as_view()),
    path('favorites/<str:comicId>', FavoritesGD.as_view()),

    # API DOCUMENTATION
    path('doc', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]


