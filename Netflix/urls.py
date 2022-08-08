from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from sqlalchemy import true


schema_view = get_schema_view(
    openapi.Info(
        title= " Films Aplacations Rest API",
        default_version= "v0",
        description="Swager dics for Rest API",
        contact=openapi.Contact("Komilov Husniddin <komilov185657@gmail.com>")
    ),
    public=True, 
    permission_classes=(AllowAny, ),
)

# import film
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('film.urls')), 
    path('token/', obtain_auth_token),
    path('docs/', schema_view.with_ui("swagger")),
    path('redoc/', schema_view.with_ui("redoc")),

]
