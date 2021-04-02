from django.urls import path
from .views import QuestionView, UsersView

app_name = 'polls'

urlpatterns = [
    path('polls/', QuestionView.as_view()),
    path('users/', UsersView.as_view()),
    path('polls/<int:pk>', QuestionView.as_view())
]