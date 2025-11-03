from django import forms

from django.forms import ModelForm
from .models import Note


class CreateNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'reminder', 'category']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 300px;',
            }),
            'text': forms.Textarea(attrs={
                'rows': 5,
                'cols': 40,  # ось тут можна зменшити ширину
                'style': 'width: 300px;',
                'class': 'form-control',
                'placeholder': 'Enter your text here',

            }),
            # 💡 Використовуємо DateTimeInput з типом "datetime-local"
            'reminder': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'style': 'width: 300px;',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'style': 'width: 300px;',
            })
        }