from .models import Stavka, Pitanja
from django import forms

class AnketeCreateForm(forms.ModelForm):
    class Meta:
        model = Stavka
        fields = ["pitanja", "tekst", "glasovi"]

# class AnketeCreateForm(forms.ModelForm):
    class Meta:
        model = Pitanja
        fields = ["pitanje"]

    def __init__(self, *args, **kwargs):
        super(AnketeCreateForm, self).__init__(*args, **kwargs)
        for fieldname in ['pitanja']:
            self.fields[fieldname].label = 'Питања'
        for fieldname in ['tekst']:
            self.fields[fieldname].label = 'Текст'
        for fieldname in ['glasovi']:
            self.fields[fieldname].label = 'Гласови'
        for fieldname in ['pitanje']:
            self.fields[fieldname].label = 'Питање'