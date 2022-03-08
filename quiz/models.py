from django.db import models
from django.utils.translation import gettext_lazy
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Quiz(models.Model):
    class Meta:
        verbose_name = gettext_lazy("Quiz")
        verbose_name_plural = gettext_lazy("Quizzes")
        ordering = ["id"]
    title = models.CharField(max_length=40)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return F'{self.title}'
    
class Question(models.Model):
    class Meta:
        ordering = ["id"]
    SCALE = (
        (0, ('Fundamental')),
        (1, ('Beginner')),
        (2, ('Intermediate')),
        (3, ('Advanced')),
        (4, ('Expert'))
    )
    TYPE = (
        (0, ("Single Choice")),
        (1, ("Multiple Choice"))
    )
    quiz_name = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="question")
    title = models.CharField(max_length=40)
    technique = models.IntegerField(choices=TYPE, default=0)
    difficulty = models.IntegerField(choices=SCALE, default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    # def changeform_link(self):
    #     if self.id:
    #         # Replace "myapp" with the name of the app containing
    #         # your Certificate model:
    #         changeform_url = reverse(
    #             'admin:myapp_certificate_change', args=(self.id,)
    #         )
    #         return u'<a href="%s" target="_blank">Details</a>' % changeform_url
    #     return u''
    # changeform_link.allow_tags = True
    # changeform_link.short_description = ''
    
    def __str__(self):
        return f'{self.quiz_name} & {self.title}'
        
    
class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
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