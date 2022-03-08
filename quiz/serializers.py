from pyexpat import model
from rest_framework import serializers
from .models import Category, Quiz, Question, Answer, Student

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'category', 'created_date', 'updated_date',)
        
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fiels = ('id', 'quiz_name', 'title', 'technique', 'difficulty', 'created_date', 'updated_date')
        
class AnswerSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question_id', 'answer_text', 'is_right', 'updated_date')
        
