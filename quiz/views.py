from rest_framework import generics
from quiz.models import Category, Question, Quiz
from django_filters.rest_framework import DjangoFilterBackend
from quiz.permissions import IsStuffOrReadOnly
from quiz.serializers import CategorySerializer, QuestionSerializer, QuizSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class QuizView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (IsStuffOrReadOnly,)
    
    def get_queryset(self):
        category = self.kwargs["category"]
        return Quiz.objects.filter(category__name=category)
    
class QuestionView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    def get_queryset(self):
        quiz = self.kwargs['quiz']
        return Question.objects.filter(quiz_name__title=quiz)