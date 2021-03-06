from rest_framework import serializers
from .models import Category, Quiz, Question, Answer, Student
        
class AnswerSerilaizer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = Answer
        fields = ('question_id', 'answer_text', 'is_right',)
        
        
class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerilaizer(many=True, read_only=True)
    quiz_id = serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = Question
        fields = ('id', 'title', 'answers', 'technique', 'difficulty', 'quiz_id')
    
    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        questions = Question.objects.create(**validated_data)
        Answer.objects.create(answers_data=questions, **answers_data)
        return answers
        

        
class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, write_only=True)
    question_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Quiz
        fields = ("title", 'question_count', 'questions')
        
    def get_question_count(self, obj):
        return obj.questions.count()
        
class CategorySerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True, write_only=True)
    quiz_count = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Category
        fields = ('name', 'quiz_count', 'quizzes')
        
    def get_quiz_count(self, obj):
        return obj.quizzes.count()
    