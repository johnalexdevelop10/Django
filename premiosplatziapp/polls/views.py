from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice
from django.utils import timezone


##def index(request):
##latest_question_list = Question.objects.all()
##    return render(request, "polls/index.html",{
##      "latest_question_list":latest_question_list
##  })

##def detail(request, question_id):
    #return HttpResponse(f"Estas viendo la pregunta numero {question_id}")
##  question = get_object_or_404(Question, pk=question_id)
##   return render(request, "polls/detail.html",{
##      "question": question
        
##  })


##def result(request, question_id):
##  question = get_object_or_404(Question, pk=question_id)
##      return render(request, "polls/result.html",{
##         "question":question
##      })

class IndexView(generic.ListView):
    template_name  = "polls/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        """Return the last five published questions"""
        #return Question.objects.order_by("-pub_date")[:8]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:8]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
  
class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/result.html"  


def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html",{
          "question": question,
          "error_message":"No elegiste una respuesta"  
        })
    else: 
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:result",args=(question.id,)))


# Create your views here.
