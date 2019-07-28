from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# from narrative.models import Story, Person
# from pages.models import AboutPage

def index(request):
  # stories = Story.objects.order_by('start_date').filter(is_published=True)

  # pageinator = Paginator(stories, 10)
  # page = request.GET.get('page')
  # paged_stories = pageinator.get_page(page)

  # context = {
  #     'stories': paged_stories,
  # }

  return render(request, 'pages/index.html')
