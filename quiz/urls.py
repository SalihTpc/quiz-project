from django.urls import path

from quiz.views import QuestionView, QuizView, CategoryListView

urlpatterns=[
    path("", CategoryListView.as_view()),
    path("<category>/", QuizView.as_view()),
    path("<category>/<quiz>/", QuestionView.as_view())
]