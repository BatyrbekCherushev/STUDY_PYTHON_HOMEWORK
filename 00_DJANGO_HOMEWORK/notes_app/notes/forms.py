from django import forms

from django.forms import ModelForm
from .models import Note


class CreateNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'reminder', 'category']

        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
            # 💡 Використовуємо DateTimeInput з типом "datetime-local"
            'reminder': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }