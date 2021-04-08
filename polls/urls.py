from django.urls import path


from .views import PollListView, PollDetailView, VoteView, QuestionListView, QuestionDetailView, AllVoteView, GetTokenView


urlpatterns = [
    path('polls/', PollListView.as_view()),
    path('polls/<int:pk>/', PollDetailView.as_view()),
    path('questions/', QuestionListView.as_view()),
    path('questions/<int:question_id>/', QuestionDetailView.as_view()),
    path('get_token/', GetTokenView.as_view()),
    path('vote/', VoteView.as_view()),
    path('get_votes/', AllVoteView.as_view()),
]