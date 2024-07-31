from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView
)


router = routers.DefaultRouter()


urlpatterns = [
    path('users/', UserCreate.as_view(), name='user-create'),
    #path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/users/me/', CurrentUser.as_view(), name='current_user'),
    path('groups/manager/users/', ManagerView.as_view(), name='manager_view'),
    path('groups/manager/users/<int:pk>', ManagerDeleteView.as_view(), name='manager_view'),
    path('groups/delivery-crew/users/', DeliveryCrewView.as_view(), name='crew_view'),
    path('groups/delivery-crew/users/<int:pk>', DeliveryCrewDeleteView.as_view(), name='crew_delete_view')
]