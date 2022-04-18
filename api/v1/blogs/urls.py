from django.urls import path
from . import views
urlpatterns = [
    path('',views.BlogList.as_view()),
    path('<str:slug>/',views.BlogRetrieveUpdateDestroy.as_view()),
    path('<str:slug>/vote/',views.VoteCreate.as_view()),
    path('<str:slug>/comments/',views.CommentList.as_view()),
    path('<str:slug>/comments/<int:pk>/', views.CommentDetail.as_view()),
]