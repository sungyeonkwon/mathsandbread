from django.db import models
from django.conf import settings
import datetime

class Quiz(models.Model):
    title = models.CharField(max_length=225, null=True)
    question = models.TextField(null=True)
    question_image = models.ImageField(upload_to='question/%Y/%m/%d/', null=True, blank=True)
    source_link = models.URLField(null=True, blank=True, unique=True)

    STATUS_CHOICES = [
        (settings.CONSTANTS['ongoing'], "Ongoing"),        
        (settings.CONSTANTS['attempted'], "Attempted"),        
        (settings.CONSTANTS['try_again'], "Try Again"),        
        (settings.CONSTANTS['completed'], "Completed"),        
        (settings.CONSTANTS['not_submitted'], "Not Submitted"),        
    ]

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default=settings.CONSTANTS['ongoing'])

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

    def __str__(self):
        return f'Quiz for EY {str(self.id)}'
    
class QuizForSY(Quiz):
    answer = models.TextField(null=True, blank=True)

    class Meta: 
        verbose_name = "Quiz For Sungyeon"
        verbose_name_plural = "Quizzes For Sungyeon"
    
    def __str__(self):
        return f'Quiz for SY {str(self.id)}'

class Bundle(models.Model):
    start_date = models.DateField(null=True)    
    is_published = models.BooleanField(default=True)
    is_bonus = models.BooleanField(default=False)
    quiz_for_EY = models.ForeignKey(QuizForEY, on_delete=models.CASCADE, null=True)
    quiz_for_SY = models.ForeignKey(QuizForSY, on_delete=models.CASCADE, null=True)

    def time_passed(self):
        today = datetime.date.today()
        timedelta = today - self.start_date 
        return timedelta.days

    def __str__(self):
        return f'Bundle starting from {str(self.start_date)}'
        