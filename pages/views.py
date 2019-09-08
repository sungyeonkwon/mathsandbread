from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django import forms
from django.contrib.auth.decorators import login_required

from quizzes.forms import ImageForm, CodeForm
from quizzes.models import Quiz, QuizForEY, QuizForSY, Bundle
from quizzes.serializers import QuizSerializer, QuizForEYSerializer, QuizForSYSerializer, BundleSerializer

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_data(request):
	bundle_data = Bundle.objects.all()
	if request.method == 'GET':
		serializer = BundleSerializer(bundle_data, many=True)
		return JsonResponse(serializer.data, safe=False)

def index(request, pk=None, category=None):

  bundles = Bundle.objects.order_by('start_date').filter(is_published=True)[::-1]
  pageinator = Paginator(bundles, 10)
  page = request.GET.get('page')
  paged_bundles = pageinator.get_page(page)
  form_ey = None
  form_sy = None

  if request.method == 'POST':
    if category == 'ey':
      quiz_instance = get_object_or_404(QuizForEY, pk=pk)
      form_ey = ImageForm(request.POST, request.FILES, instance=quiz_instance)
      if form_ey.is_valid():
        form_ey.save()
    elif category == 'sy':
      quiz_instance = get_object_or_404(QuizForSY, pk=pk)
      form_sy = CodeForm(request.POST, instance=quiz_instance)
      if form_sy.is_valid():
        form_sy.save()
      return redirect('index')
  else:
    form_ey = ImageForm(auto_id='id_for_%s', label_suffix='')
    form_sy = CodeForm(auto_id='id_for_%s', label_suffix='')

  context = {
      'bundles': paged_bundles,
      'form_ey': form_ey,
      'form_sy': form_sy,
  }

  return render(request, 'pages/index.html', context)




  