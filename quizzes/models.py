from django.db import models
from datetime import datetime


class Quiz(models.Model):
    title = models.CharField(max_length=225, null=True)
    question = models.TextField(null=True)
    source_link = models.URLField(null=True, blank=True)

    ONGOING = "Ongoing"
    PENDING = "Pending"
    TRY_AGAIN = "Try again?"
    COMPLETED = "YAY!"
    NOT_SUBMITTED = "You didn't like this quiz!"

    STATUS_CHOICES = [
        (ONGOING, "Ongoing"),        
        (PENDING, "Pending"),        
        (TRY_AGAIN, "Try Again"),        
        (COMPLETED, "Completed"),        
        (NOT_SUBMITTED, "Not Submitted"),        
    ]

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default=ONGOING)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

class QuizForEY(Quiz):
    answer = models.ImageField(upload_to='answer_ey/%Y/%m/%d/', null=True, blank=True)

    class Meta: 
        verbose_name = "Quiz For Eunyoung"
        verbose_name_plural = "Quizzes For Eunyoung"

class QuizForSY(Quiz):
    answer = models.TextField(null=True, blank=True)

    class Meta: 
        verbose_name = "Quiz For Sungyeon"
        verbose_name_plural = "Quizzes For Sungyeon"

class Bundle(models.Model):
    start_date = models.DateField(null=True)    
    is_published = models.BooleanField(default=True)
    quiz_for_EY = models.ForeignKey(QuizForEY, on_delete=models.CASCADE)
    quiz_for_SY = models.ForeignKey(QuizForSY, on_delete=models.CASCADE)

    def __str__(self):
        return f'Bundle starting from {str(self.start_date)}'