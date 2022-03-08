from pyexpat import model
from django.contrib import admin
from .models import Category, Quiz, Question, Answer, Student


admin.site.register(Student)

class QuestionInlineModel(admin.TabularInline):
    model = Question
    fields = ['title', 'technique', 'difficulty']
    extra = 2
    
class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        'answer_text', 
        'is_right'
        ]
    extra = 4
    
# class QuestionLinkInline(admin.TabularInline):
#     model = Question
#     # Whichever fields you want: (I usually use only a couple
#     # needed to identify the entry)
#     fields = ('title', 'technique', 'difficulty','changeform_link')
#     readonly_fields = ('changeform_link', )
#     extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = [
        'name',
        ]
    
    
@admin.register(Quiz)    
class QuizAdmin(admin.ModelAdmin):
    model = Quiz
    list_display = [
        'id', 
        'title',
        ]
    inlines = [
        QuestionInlineModel
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    model = Question
    fields = [
        'title',
        'quiz_name',
        ]
    list_display = [
        'title', 
        'quiz_name',
        'updated_date'
        ]
    inlines = [
        AnswerInlineModel, 
        ]
    
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'question_id',
        'answer_text', 
        'is_right',
        ]