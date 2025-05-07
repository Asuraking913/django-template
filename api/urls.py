from os import name
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.serializers import CreateListFoodMenuSerializer
from .views import CreateFoodMenuView, RegisterUserView 

urlpatterns = [
    # path("", BaseView.as_view(), name="Base url view"),
    # auth
    path("get-token/", TokenObtainPairView.as_view(), name='Obtain Token'),
    path("refresh/", TokenRefreshView.as_view(), name='Refresh Token'),
    path("verfiy-token/", TokenVerifyView.as_view(), name='Verify token'),
    path("register/", RegisterUserView.as_view(), name='Register User'), 

    # menu
    path("create-menu/", CreateFoodMenuView.as_view(), name='Create food menu'), 
]
