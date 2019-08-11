from django.forms import ModelForm
from django.conf import settings
from .models import QuizForEY, QuizForSY
from django.shortcuts import get_object_or_404

class ImageForm(ModelForm):
    """ Image Upload form """

    def save(self, commit=True):
        form = super(ImageForm, self).save(commit=False)
        answer = self.cleaned_data['answer']

        quiz_instance = get_object_or_404(QuizForEY, pk=form.pk)

        if answer:
            form.answer = answer
            form.status = settings.CONSTANTS['attempted']
        
        form.save()
        return form

    class Meta:
        model = QuizForEY
        fields = ('answer', )

class CodeForm(ModelForm):
    """ Code Upload form """

    def save(self, commit=True):
        form = super(CodeForm, self).save(commit=False)
        answer = self.cleaned_data['answer']

        quiz_instance = get_object_or_404(QuizForSY, pk=form.pk)

        if answer:
            form.answer = answer
            form.status = settings.CONSTANTS['attempted']

        form.save()
        return form

    class Meta:
        model = QuizForSY
        fields = ('answer', )