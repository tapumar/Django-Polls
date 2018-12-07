from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Poll, Choice, Vote
from .serializers import PollSerializer


def polls_list(request):
    MAX_OBJECTS = 20

    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values("question",
                                         "pub_date"))}
    return JsonResponse(data)


def vote(request, question_id):
    vote = Vote()
    question = Poll.objects.filter(id=question_id).first()
    try:
        selected_choice = Choice.objects.filter(
            id=request.POST['choice']).first()
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/poll_vote.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        vote.poll = question
        vote.choice = selected_choice
        vote.save()
        votes, total = checkVotes(question_id)
        return HttpResponseRedirect(
            reverse('polls:polls_detail', args=(question_id,)),
            {'votes': votes.items(), 'total': total}
        )


def checkVotes(question_id):
    question = Poll.objects.filter(id=question_id).first()
    votes = Vote.objects.filter(poll=question)
    choices = Choice.objects.filter(poll=question)
    voted_choices = {}
    total = 0
    for choice in choices:
        voted_choices[choice.choice_text] = 0
    for vote in votes:
        if vote.choice in choices:
            voted_choices[vote.choice.choice_text] += 1
            total += 1

    return voted_choices, total


class VoteDetail(generic.DetailView):
    model = Poll
    template_name = 'polls/poll_vote.html'

    def get_context_data(self, **kwargs):
        poll = Poll.objects.filter(id=self.kwargs['pk']).first()
        choices = Choice.objects.filter(poll=poll)
        context = {'poll': poll, 'choices': choices}
        return context


class PollDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'polls/poll_detail.html'

    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        choices = Choice.objects.filter(poll=poll)
        serializer = PollSerializer(poll)
        votes, total = checkVotes(pk)
        return Response(
            {'serializer': serializer, 'poll': poll,
             'choices': choices, 'votes': votes.items(), 'total': total}
        )


class PollList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'polls/polls_list.html'

    def get(self, request):
        polls = Poll.objects.filter().all()
        serializer = PollSerializer(polls)
        return Response({'serializer': serializer, 'polls': polls})
