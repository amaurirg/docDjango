from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello World em Python com Django!")

def detail(request, question_id):
    return HttpResponse("Você está na questão %s" % question_id)

def results(request, question_id):
    response = "Estes são os resultados da pergunta %s", % question_id
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Você está votando na questão %s" % question_id)
