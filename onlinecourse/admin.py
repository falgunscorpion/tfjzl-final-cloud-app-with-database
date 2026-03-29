from django.contrib import admin
from .models import Course, Lesson, Enrollment, Question, Choice, Submission

# Inline for Choices inside Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

# Inline for Questions inside Lesson
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Lesson Admin (FIXED with list_display)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    inlines = [QuestionInline]

# Course Admin (IMPORTANT — REQUIRED)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('name',)
    inlines = [LessonInline] if 'LessonInline' in globals() else []

# Register models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
