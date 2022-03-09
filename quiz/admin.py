from django.contrib.admin import TabularInline, StackedInline, site
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin
from django.contrib import admin
from .models import Category, Quiz, Question, Answer, Student


admin.site.register(Student)

class AnswerInlineModel(SuperInlineModelAdmin, TabularInline):
    model = Answer
    fields = [
        'answer_text', 
        'is_right'
        ]
    extra = 4
    
class QuestionInlineModel(SuperInlineModelAdmin, StackedInline):
    model = Question
    fields = ['title', 'technique', 'difficulty']
    extra = 1
    inlines = (AnswerInlineModel,)
    

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
    
# @admin.register(Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     model = Answer
#     list_display = [
#         'question_id',
#         'answer_text', 
#         'is_right',
#         ]
