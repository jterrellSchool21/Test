from django.db import models
from datetime import datetime, timedelta

class Poll(models.Model):
    name = models.CharField(max_length=120)
    date_start = models.DateTimeField(default=datetime.now())
    date_end = models.DateTimeField(default=datetime.now() + timedelta(days=1))

class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    answer_type = models.IntegerField()

class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)

class Token(models.Model):
    token = models.CharField(max_length=120, unique=True)
    questions = models.ManyToManyField(Question, related_name='tokens')
    answers = models.ManyToManyField(Answer, related_name='answers')