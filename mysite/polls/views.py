from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def Index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_question_list }
    return render(request, 'polls/index.html', context)
## Create a utility views


def Results(request, question_id):
    question = Question(pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def Vote(request, question_id):
    return f'Você está votando na questão de número {question_id}'