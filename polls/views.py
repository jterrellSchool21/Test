from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import Question, Users, Answer
from .serializers import QuestionSerializer, UsersSerializer

import os
import binascii

class QuestionView(APIView):
    def get(self, request):
        objects = Question.objects.all().filter(is_active=True)
        serializer = QuestionSerializer(objects, many=True)
        return Response({"Active": serializer.data})

    def post(self, request):
        question = request.data.get("Active")
        serializer = QuestionSerializer(data=question)
        if serializer.is_valid(raise_exception=True):
            question_saved = serializer.save()
        return Response({"success": "Question '{}' created successfully".format(question_saved.title)})

    def put(self, request, pk):
        saved_question = get_object_or_404(Question.objects.all(), pk=pk)
        data = request.data.get('Active')
        serializer = QuestionSerializer(instance=saved_question, data=data, partial=True)
        # data = request.data.get('Active')
        # serializer = QuestionSerializer(instance=saved_question, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            question_saved = serializer.save()
        return Response({
            "success": "Question '{}' updated successfully".format(question_saved.title)
        })
    
    def delete(self, request, pk):
        question = get_object_or_404(Article.objects.all(), pk=pk)
        question.delete()
        return Response({
            "message": "Question with id '{}' has been deleted.".format(pk)
        }, status=204)

class UsersView(APIView):
    def get(self, request):
        token = binascii.hexlify(os.urandom(20)).decode()
        user = UsersSerializer({"token": token})
        # Users.objects.create(user)
        return Response({"token": token})

    def post(self, request):
        answer = request.data.get("Answer")
        data = UsersSerializer(data)
        Users.objects.filter(token == data.token).update(question_id = data.question_id)
        Answer.objects.filter(answer_id == int(data.question_id.split('_')[1])).update(votes = votes + 1)