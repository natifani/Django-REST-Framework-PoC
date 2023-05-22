from django.db import models
from jsonfield import *
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.category

class Quiz(models.Model):
    title = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_data")
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    points = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True)

    def __str__(self):
        return self.quiz

class Question(models.Model):
    question = models.CharField(max_length=300)
    answers = JSONField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="quiz_data")

    def __str__(self):
        return self.question
