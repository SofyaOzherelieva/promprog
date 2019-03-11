from django.shortcuts import redirect
from django.shortcuts import render
from .models import Question


def index(request):
    questions = Question.objects.all()
    context = {"questions": questions}
    return render(request, 'questionnarie/index.html', context)


def new_question(request):
    question = Question(
        text=request.POST.get("questions", "")
    )
    question.save()
    return redirect('/')


