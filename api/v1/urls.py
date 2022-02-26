from django.urls import path,include

urlpatterns = [
    path('accounts/',include('api.v1.accounts.urls')),
    path('profiles/',include('api.v1.customers.urls')),
]