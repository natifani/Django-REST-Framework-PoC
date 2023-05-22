from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from quizzes_api.models import Quiz
from quizzes_api.serializers import QuizSerializer, QuizNestedSerializer
import json

class QuizViewSet(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        '''
        List all the quizzes
        '''
        
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        '''
        Create a quiz
        '''
       
        data = {
            "title": request.data.get("title"),
            "category": request.data.get("category"),
            "points": request.data.get("points"),
            "description": request.data.get("description")
        }

        serializer = QuizSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, id=None):
        '''
        Get quiz by id
        '''

        if not Quiz.objects.filter(id=id).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        quiz = Quiz.objects.get(id=id)
        serializer = QuizNestedSerializer(quiz)
        print(serializer.data)

        for ii in serializer.data['questions']:
            ii['answers'] =  json.loads(ii['answers'])
            
        return Response(serializer.data, status=status.HTTP_200_OK)


    def destroy(self, request, id=None):
        '''
        Delete a quiz
        '''

        if Quiz.objects.filter(id=id).exists():
            quizzes = Quiz.objects.get(id=id)
            quizzes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)