from django import forms
from .models import Topic, Notes

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        
class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}