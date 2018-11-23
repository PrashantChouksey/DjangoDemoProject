from django.shortcuts import render, get_object_or_404
from .models import Question
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    l_qus = Question.objects.order_by('-pub_date')[:5]
    context = {'l_qus':l_qus}
    return render(request, 'polls/index.html', context=context)

def detail(request, q_id):
    qus = get_object_or_404(Question, pk=q_id)
    return render(request, "polls/detail.html", context={'qus':qus})

def results(req, q_id):

    qus =  get_object_or_404(Question, pk=q_id)
    return render(req, 'polls/results.html', context={'qus':qus})

def vote(req, q_id):
    qus = get_object_or_404(Question, pk=q_id)
    try:
        selected_choice = qus.choice_set.get(pk = req.POST['choice'])
    except:
        return render(req, "polls:detail.html", {'qus':qus, 'error_message': "Please Select a choice"})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(qus.id,)))
