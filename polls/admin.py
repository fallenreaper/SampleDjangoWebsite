from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    """Stacks [extra] number of Choices inline with the below QuestionAdmin"""
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """Instead of just having questions, you can customize the layout and add nested items."""
    fieldsets = [
        (None,{'fields':['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)