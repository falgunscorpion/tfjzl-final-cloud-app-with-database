from django.shortcuts import render
from .models import *

def submit(request, course_id):
    if request.method == 'POST':
        choices = request.POST.getlist('choice')
        submission = Submission.objects.create()
        submission.choices.set(choices)
        return show_exam_result(request, course_id)

def show_exam_result(request, course_id):
    return render(request, 'exam_result.html')
