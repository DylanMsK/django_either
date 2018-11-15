from django.db import models
from django.conf import settings


# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    answerA = models.CharField(max_length=50)
    answerB = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_list = [['A', 'left'], ['B', 'right']]
    answer = models.CharField(max_length=100, choices=answer_list)
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return self.content
        
