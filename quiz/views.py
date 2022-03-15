from rest_framework import generics
from quiz.models import Category, Question, Quiz
from django_filters.rest_framework import DjangoFilterBackend
from quiz.permissions import IsStuffOrReadOnly
from quiz.serializers import CategorySerializer, QuestionSerializer, QuizSerializer
from rest_framework.permissions import IsAuthenticated

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class QuizView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    
    
    def get_queryset(self):
        category = self.kwargs["category"].title().replace(("-"), (" "))
        return Quiz.objects.filter(category__name=category)
    
class QuestionView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        quiz = self.kwargs['quiz'].title().replace(("-"), (" "))
        return Question.objects.filter(quiz_name__title=quiz)