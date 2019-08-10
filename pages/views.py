from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django import forms
from django.contrib.auth.decorators import login_required

from quizzes.forms import ImageForm
from quizzes.models import QuizForEY, QuizForSY, Bundle

def index(request, pk=None):

  bundles = Bundle.objects.order_by('start_date').filter(is_published=True)[::-1]

  pageinator = Paginator(bundles, 10)
  page = request.GET.get('page')
  paged_bundles = pageinator.get_page(page)

  if request.method == 'POST':
    print("need to get a pk", pk)
    quiz_instance = get_object_or_404(QuizForEY, pk=pk)
    print("request.POST", request.POST)

    form = ImageForm(request.POST, request.FILES, instance=quiz_instance)
    if form.is_valid():
      form.save()
      return HttpResponse('good! uploaded well')
  else:
    form = ImageForm()

  context = {
      'bundles': paged_bundles,
      'form': form,
  }

  return render(request, 'pages/index.html', context)




  