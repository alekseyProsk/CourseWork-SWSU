from _datetime import date

from .models import Appeal
from django.forms import ModelForm, Textarea, TextInput


class AppealForm(ModelForm):
    class Meta:
        model = Appeal
        fields = ["theme", "textAppeal"]
        widgets = {
            "theme": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите тему обращения'
            }),
            "textAppeal": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст обращения'
            })

        }
