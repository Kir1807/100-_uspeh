from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView

class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/Mytest.html'

def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk = pk)
    return render(request, 'quizes/Test.html', {'obj': quiz})
