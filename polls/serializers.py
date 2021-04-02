from .models import Question, Users
from rest_framework import serializers

class QuestionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    date_published = serializers.DateTimeField()
    is_active = serializers.BooleanField()
    date_end = serializers.DateTimeField()
    question_id = serializers.IntegerField()
    def create(self, validated_data):
        return Question.objects.create(**validated_data)
    def update(self, instance, validated_data, pk):
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.date_end = validated_data.get('date_end', instance.date_end)
        instance.save()
        return instance

class UsersSerializer(serializers.Serializer):
    token = serializers.CharField(max_length = 200)
    question_id = serializers.CharField(max_length=200)
    def create(self, val_data):
        Users.objects.create(**val_data)