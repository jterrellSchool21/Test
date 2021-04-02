import datetime
from django.db import models
  
  
class Question(models.Model):
    """Вопрос"""
    title = models.CharField(max_length=200, verbose_name = "Вопрос")
    date_published = models.DateTimeField(verbose_name = "Дата публикации", 
        default = datetime.datetime.now())
    is_active = models.BooleanField(verbose_name = "Дествующий")
    date_end = models.DateTimeField(verbose_name = "Дата окончания",
        default = datetime.datetime.now() + datetime.timedelta(days=1))
    question_id = models.IntegerField(verbose_name="Id опроса")
    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title
 
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    """Вариант ответа на вопрос"""
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, verbose_name = "Ответ")
    votes = models.IntegerField(verbose_name = "Голосов", default = 0)
    answer_id = models.IntegerField(verbose_name = "Id вопроса")
    def __unicode__(self):
        return self.answer

    def __str__(self):
        return self.answer
 
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class Users(models.Model):
    token = models.CharField(max_length = 200, verbose_name="Token")
    question_id = models.CharField(max_length=200, verbose_name = "Id")
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    def __str__(self):
        return self.answer