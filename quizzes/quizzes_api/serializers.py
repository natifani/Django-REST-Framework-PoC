from rest_framework import serializers
from .models import Category, Quiz, Question

# Create your serializers here.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category"]

class CategoryNestedSerializer(serializers.ModelSerializer):
    quizzes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Category
        fields = ["id", "category", "quizzes"]

    def get_quizzes(self, obj):
        return QuizSerializer(obj.category_data, many=True).data

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ["id", "title", "category", "points", "description", "created"]

class QuizNestedSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Quiz
        fields = ["id", "title", "category", "points", "description", "created", "questions"]

    def get_questions(self, obj):
        return QuestionSerializer(obj.quiz_data, many=True).data

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "question", "answers", "quiz"]