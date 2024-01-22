from django import forms

from . import models


class CreatePersonForm(forms.ModelForm):
    phones = forms.CharField(widget=forms.Textarea(), help_text="разделитель с новой строки '\\n'")

    class Meta:
        model = models.Persone
        fields = (
            'name',
            'phones'
        )
