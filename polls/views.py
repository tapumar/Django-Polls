from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Poll
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

class PollDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'polls/poll_detail.html'

    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        serializer = PollSerializer(poll)
        return Response({'serializer': serializer, 'poll': poll})

    def post(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        serializer = PollSerializer(poll, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'poll': poll})
        serializer.save()
        return redirect('polls-list')

class PollList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'polls/poll_list.html'

    def get(self, request, pk):
        poll = Poll.objects.get().all()
        serializer = PollSerializer(poll)
        return Response({'serializer': serializer, 'poll': poll})

    def post(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        serializer = PollSerializer(poll, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'poll': poll})
        serializer.save()
        return redirect('polls-list')
