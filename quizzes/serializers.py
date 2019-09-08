from .models import Quiz, QuizForEY, QuizForSY, Bundle
from rest_framework import serializers

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = [
          'title', 
          'question', 
          'question_image', 
          'source_link',
          'status',
        ]


class QuizForEYSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizForEY
        fields = [
          'answer', 
        ]

class QuizForSYSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizForSY
        fields = [
          'answer', 
        ]

class BundleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bundle
        fields = [
          'start_date', 
          'is_published', 
          'is_bonus', 
          'quiz_for_EY', 
          'quiz_for_SY', 
        ]