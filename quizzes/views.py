# from django.shortcuts import render, HttpResponseRedirect
# from django.http import HttpResponse, JsonResponse

# from .models import Quiz, QuizForEY, QuizForSY, Bundle
# from .serializers import QuizSerializer, QuizForEYSerializer, QuizForSYSerializer, BundleSerializer

# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def get_data(request):
# 	data = Quiz.objects.all()
# 	if request.method == 'GET':
# 		serializer = QuizSerializer(data, many=True)
# 		return JsonResponse(serializer.data, safe=False)
