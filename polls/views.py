from rest_framework.generics import (
    get_object_or_404,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from rest_framework.views import APIView

from .models import Token, Question, Poll, Answer
from .serializers import *
from datetime import datetime

class PollListView(ListCreateAPIView):
    queryset = Poll.objects.filter(date_end__gte = datetime.now())
    serializer_class = PollSerializer

class PollDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class QuestionListView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class GetTokenView(APIView):
    def get(self, request):
        token = binascii.hexlify(os.urandom(20)).decode()
        token_serialize = TokenSerializer(request.data)
        token_serialize.is_valid(raise_exception=True)
        token_serialize.save()

class VoteView(APIView):
    def post(self, request):
        token_id = request.META.get('Token')
        if not token_id:
            return Response(status=403)
        question_id = request.data.get("question_id")
        answer_type = Question.objects.filter(questions=qeustion_id).get("answer_type")
        if answer_type == 1:
            answer_serialize = answer1(request.data)
        elif answer_type == 2:
            answer_serialize = answer2(request.data)
        elif answer_type == 3:
            answer_serialize = answer3(request.data)
        token = Token.object.filter(id=token_id).first()
        if token.questions.filter(pk=Question_id).exists():
            return Response(status=403)
        else:
            answer_serialize.is_valid(raise_exception=True)
            answer_serialize.save()

class AllVoteView(APIView):
    def get(self, request):
        token_id = request.META.get("Token")
        questions = Token.objects.filter(token=token_id)
        return Response({"questions": questions.get("questions"), "answers": questions.get("answers")}, status=200)