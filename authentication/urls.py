from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authantication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authantication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
