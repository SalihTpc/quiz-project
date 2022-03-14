from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
    
class Quiz(models.Model):
    class Meta:
        verbose_name = gettext_lazy("Quiz")
        verbose_name_plural = gettext_lazy("Quizzes")
        ordering = ["id"]
    title = models.CharField(max_length=40)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="quizzes")
    
    def __str__(self):
        return F'{self.title}'
    
class Question(models.Model):
    class Meta:
        ordering = ["id"]
    SCALE = (
        (0, gettext_lazy('Fundamental')),
        (1, gettext_lazy('Beginner')),
        (2, gettext_lazy('Intermediate')),
        (3, gettext_lazy('Advanced')),
        (4, gettext_lazy('Expert'))
    )
    TYPE = (
        (0, gettext_lazy("Single Choice")),
        (1, gettext_lazy("Multiple Choice"))
    )
    quiz_name = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    title = models.CharField(max_length=255)
    technique = models.IntegerField(choices=TYPE, default=0)
    difficulty = models.IntegerField(choices=SCALE, default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.quiz_name} & {self.title}'
        
    
class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=255)
    is_right = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    
class Student(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    phoneNumber = models.IntegerField()
    updateDate = models.DateTimeField(auto_now=True)
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'