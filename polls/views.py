from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Poll, Choice, Vote
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from .serializers import PollSerializer


def polls_list(request):
    MAX_OBJECTS = 20

    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values("question",
                                         "created_by__username",
                                         "pub_date"))}
    return JsonResponse(data)

def vote(request, question_id):
    vote = Vote()
    question = Poll.objects.filter(id=question_id).first()
    try:
        selected_choice = Choice.objects.filter(id=request.POST['choice']).first()
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/poll_vote.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        vote.poll = question
        vote.choice = selected_choice
        vote.save()
        votos = Vote.objects.filter(poll=question)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:polls_detail', args=(question_id,)),{'votos':votos})


class VoteDetail(generic.DetailView):
    model = Poll
    template_name = 'polls/poll_vote.html'

    def get_context_data(self, **kwargs):
        poll = Poll.objects.filter(id=self.kwargs['pk']).first()
        choices = Choice.objects.filter(poll=poll)
        context = {'poll': poll, 'choices':choices}
        return context


class PollDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'polls/poll_detail.html'

    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        choices = Choice.objects.filter(poll=poll)
        # for choice in choices:
        #     votes = Vote.objects.filter(poll=poll,choice=choice).count()
        #     porc += votes
        serializer = PollSerializer(poll)
        return Response(
            {'serializer': serializer, 'poll': poll, 'choices': choices}
        )

    # def post(self, request, pk):
    #     poll = get_object_or_404(Poll, pk=pk)
    #     serializer = PollSerializer(poll, data=request.data)
    #     if not serializer.is_valid():
    #         return Response({'serializer': serializer, 'poll': poll})
    #     serializer.save()
    #     return redirect('polls-list')


class PollList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'polls/polls_list.html'

    def get(self, request):
        polls = Poll.objects.filter().all()
        serializer = PollSerializer(polls)
        return Response({'serializer': serializer, 'polls': polls})

    # def post(self, request, pk):
    #     poll = get_object_or_404(Poll, pk=pk)
    #     serializer = PollSerializer(poll, data=request.data)
    #     if not serializer.is_valid():
    #         return Response({'serializer': serializer, 'poll': poll})
    #     serializer.save()
    #     return redirect('polls-list')
