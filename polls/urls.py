from django.urls import path
from polls import views

urlpatterns = [
    path('polls/', views.PollListView.as_view()),
    path('polls/<int:pk>/', views.PollDetail.as_view()),
]