from django.shortcuts import render

def admin(request):
    return render(request, 'autorize/moffice.html')


def gl(request):
    return render(request, 'autorize/Home.html')


def login(request):
    return render(request, 'account/login.html')


def logout(request):
    return render(request, 'account/logout.html')


def profile(request):
    return render(request, 'autorize/Mytest.html')


def results(request):
    return render(request, 'autorize/UResults.html')


def access(request):
    return render(request, 'autorize/Access.html')


def consultation(request):
    return render(request, 'autorize/UConsultation.html')




