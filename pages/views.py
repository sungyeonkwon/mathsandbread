from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from quizzes.models import QuizForEY, QuizForSY, Bundle

def index(request):
  bundles = Bundle.objects.order_by('start_date').filter(is_published=True)[::-1]

  pageinator = Paginator(bundles, 10)
  page = request.GET.get('page')
  paged_bundles = pageinator.get_page(page)

  context = {
      'bundles': paged_bundles,
  }

  return render(request, 'pages/index.html', context)
