from django.shortcuts import render
from .models import Question, Quiz
from django.views.generic import ListView
from django.http import JsonResponse

# class QuizListView(ListView):
#     model = Quiz
#     template_name: str = 'autorize/Mytest.html'

# def quiz_view(request, pk):
#     quiz = Quiz.objects.get(pk=pk)
#     return render(request, 'autorize/base.html', {'obj': quiz})

# def quiz_data_view(request, pk):
#     quiz = Quiz.objects.get(pk=pk)
#     questions = []
#     for q in quiz.get_questions():
#         answers = []
#         for a in q.get_answers():
#             answers.append(a.text)
#         questions.append({str(q): answers})
#     return JsonResponse ({
#         'data': questions,
#         'time': quiz.time
#     })


def gl(request):
    return render(request, 'autorize/Home.html')


def login(request):
    return render(request, 'account/login.html')

def logout(request):
    return render(request, 'account/logout.html')


def profile(request):
    return render(request, 'autorize/User.html')


def mytest(request):
    return render(request, 'autorize/Mytest.html')


def test(request):
    return render(request, 'autorize/Test.html')


def results(request):
    return render(request, 'autorize/UResults.html')


def access(request):
    return render(request, 'autorize/Access.html')


def results(request):
    return render(request, 'autorize/UResults.html')


def consultation(request):
    return render(request, 'autorize/UConsultation.html')




