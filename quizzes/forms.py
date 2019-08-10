from django.forms import ModelForm
from .models import QuizForEY
from django.shortcuts import get_object_or_404

class ImageForm(ModelForm):
    """ Image Uploade form """

    def save(self, commit=True):
        print('hello this is called')
        form = super(ImageForm, self).save(commit=False)
        answer = self.cleaned_data['answer']

        quiz_instance = get_object_or_404(QuizForEY, pk=form.pk)
        quiz_instance.answer = answer
        print("answer", answer)
        print("quix anser", quiz_instance.answer)
        
        print('what is the pk?', form.pk)

        if answer:
            form.answer = answer
        
        form.save()
        return form

    class Meta:
        model = QuizForEY
        fields = ('answer', )
