from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('',views.UserRetrieveUpdateAPIView.as_view()),
    path('register/',views.RegisterView.as_view()),
    path('login/',views.MyTokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('change_password/<int:pk>',views.ChangePasswordView.as_view()),
]