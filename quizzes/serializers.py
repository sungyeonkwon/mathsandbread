from .models import Quiz, QuizForEY, QuizForSY, Bundle
from rest_framework import serializers

class QuizSerializer(serializers.ModelSerializer):
  class Meta:
      model = Quiz
      fields = '__all__'
      # fields = [
      #   'title', 
      #   'question', 
      #   'question_image', 
      #   'source_link',
      #   'status',
      # ]


class QuizForEYSerializer(serializers.ModelSerializer):
  class Meta:
      model = QuizForEY
      fields = '__all__'
      # fields = [
      #   'answer', 
      # ]

class QuizForSYSerializer(serializers.ModelSerializer):
  class Meta:
      model = QuizForSY
      fields = '__all__'
      # fields = [
      #   'answer', 
      # ]

class BundleSerializer(serializers.ModelSerializer):
  quiz_for_EY = QuizForEYSerializer()
  quiz_for_SY = QuizForSYSerializer()
  class Meta:
      model = Bundle
      fields = '__all__'
      # fields = [
      #   'start_date', 
      #   'is_published', 
      #   'is_bonus', 
      #   'quiz_for_EY', 
      #   'quiz_for_SY', 
      # ]