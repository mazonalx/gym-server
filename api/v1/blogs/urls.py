from django.urls import path
from . import views
urlpatterns = [
    path('',views.BlogList.as_view(),name='blog-list'),
    path('<str:slug>/',views.BlogRetrieveUpdateDestroy.as_view(),name='blog-detail'),
    path('<str:slug>/vote/',views.VoteCreate.as_view()),
    path('<str:slug>/comments/',views.CommentList.as_view(),name='comment-list'),
    path('<str:slug>/comments/<int:pk>/', views.CommentDetail.as_view(),name='comment-detail'),
]