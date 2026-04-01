from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission

# Inline for Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# Inline for Question
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'lesson']
    inlines = [ChoiceInline]

# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
    inlines = [QuestionInline]

# Register models
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
