"""
URL configuration for CourseDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from allauth.account.views import LogoutView
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from game_store import viewsets
from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Game Store API",
        default_version='v1',
        description="API documentation for Game Store",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register('customer', viewsets.CustomerViewSet)
router.register('developer', viewsets.DeveloperViewSet)
router.register('discount', viewsets.DiscountViewSet)
router.register('games', viewsets.GameViewSet)
router.register('genre', viewsets.GenreViewSet)
router.register('inventory', viewsets.InventoryViewSet)
router.register('order', viewsets.OrderViewSet)
router.register('platform', viewsets.PlatformViewSet)
router.register('publisher', viewsets.PublisherViewSet)
router.register('review', viewsets.ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api-auth/login/', include('rest_framework.urls')),
    # path('api-registration/', registration),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('register/', views.RegisterView.as_view(), name='register'),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path("", TemplateView.as_view(template_name="index.html")),

    path('accounts/', include('allauth.urls')),
    path("logout/", LogoutView.as_view()),
]
