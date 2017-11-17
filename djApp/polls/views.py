from django.shortcuts import get_object_or_404, render
from .models import Questions


# def index(request):
#     latest_question_list = Questions.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', locals())

def detail(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'polls/detail.html', locals())

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
