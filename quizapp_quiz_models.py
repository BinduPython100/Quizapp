from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Quiz(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)
    
    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)
    
    def __str__(self):
        return self.text


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=10, null=True)
    address = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
    def firstname(self):
        return self.user.first_name
    
    def lastname(self):
        return self.user.last_name
    
    def email(self):
        return self.user.email
