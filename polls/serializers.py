from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import Poll, Question, Answer, Token
from django.core.validators import int_list_validator

class PollSerializer(ModelSerializer):

    class Meta:
        model = Poll
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.date_end = validated_data.get('date_end', instance.date_end)
        return instance

class AnswerSerializer():
    class Meta:
        model = Answer
        fields = '__all__'

class TokenSerializer(ModelSerializer):
    class Meta:
        model = Token
        fields = "__all__"
    
    def create(self, validated_data):
        Token.objects.create(**validated_data)

class answer1(Serializer):
    queistion_id = serializers.IntegerField()

class answer2(Serializer):
    question_id = serializers.ListField(child=serializers.IntegerField(min_value=0, max_value=100))

class answer3(Serializer):
    question_id = serializers.CharField()

class QuestionSerializer(ModelSerializer):
    answers = AnswerSerializer()

    class Meta:
        model = Question
        fields = '__all__'

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        question = Question.objects.create(**validated_data)
        for answer_data in answers_data:
            Answer.objects.create(question=question, **answer_data)
        return question

    def update(self, instance, validated_data):
        answers_data = validated_data.pop('answer')

        instance.answers.delete()

        for answer_data in answers_data:
            Answer.objects.create(question=instance, **answer_data)

        instance.name = validated_data.get('name', instance.name)

        instance.save()