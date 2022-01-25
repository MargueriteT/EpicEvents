"""EpicEvents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import AllUsersViewSet
from clients.views import ClientsViewSet
from contracts.views import AllContractsViewSet
from events.views import EventsViewSet


router = routers.SimpleRouter()

# List of clients
router.register(r'clients', ClientsViewSet, basename='clients')


# List of all users and access to details
router.register(r'users', AllUsersViewSet, basename='users')


# List of all users and access to details
router.register(r'contracts', AllContractsViewSet, basename='contracts')


# List of all users and access to details
router.register(r'events', EventsViewSet, basename='events')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
