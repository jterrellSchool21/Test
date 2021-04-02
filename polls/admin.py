from django.contrib import admin
from .models import Question, Answer, Users
 
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2

# class Users_id(admin.TabularInline):
#     model = Users

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'is_active', 'question_id')
    list_filter = ['date_published']
    search_fields = ['title']
    fieldsets = [
        (None, 
            {'fields': ['title', 'is_active']}
        ),
        ('Информация о дате',
            {'fields': ['date_published'], 
            'classes': ['collapse']}
        ),
    ]
    inlines = [AnswerInline]
 
admin.site.register(Question, QuestionAdmin)