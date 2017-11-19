from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choise, Questions


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Questions.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Questions
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Questions
    template_name = 'polls/results.html'

def vote(request, question_id):
    questions = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = questions.choise_set.get(pk=request.POST['choice'])
    except (KeyError, Choise.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'questions': questions,
            'error_message': "Вы не выбрали вариант ответа",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(questions.id,)))
