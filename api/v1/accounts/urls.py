from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('',views.UserRetrieveUpdateAPIView.as_view()),
    path('register/',views.RegisterView.as_view()),
    path('login/',views.MyTokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('change_password/<int:pk>/',views.ChangePasswordView.as_view()),
]
# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0NTQyODY3MiwiaWF0IjoxNjQ1MzQyMjcyLCJqdGkiOiJhMmZlODdjNWViZDM0MDc2OWFhYTg2YTRmZTE1NTQ3ZiIsInVzZXJfaWQiOjJ9.QKGWYEvC-dY5OVZS3WXM_4Tkf8fp72edvCqiNUdLpw4",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ1MzQyNTcyLCJpYXQiOjE2NDUzNDIyNzIsImp0aSI6IjlkMTIzMTAwZjI3MDRkY2M4YWU3Y2I1OGVkNmMwYTUxIiwidXNlcl9pZCI6Mn0.yPFwsRB5sCOS-FTJHtIhGQcjTF3cEeie9uMLxNybAQI",
#     "username": "sampleuser"
# }