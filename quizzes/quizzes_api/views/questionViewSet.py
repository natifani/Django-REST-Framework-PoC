from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from quizzes_api.models import Question
from quizzes_api.serializers import QuestionSerializer
import json

class QuestionViewSet(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        '''
        List all the questions
        '''
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)

        for item in serializer.data:
            item['answers'] = json.loads(item['answers'])

        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        '''
        Create a question
        '''
       
        data = {
            "quiz": request.data.get("quiz"),
            "question": request.data.get("question"),
            "answers": json.dumps(request.data.get("answers"))
            #
            # "answers": {"incorrect": [..], "correct": [..]}
            #
        }

        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, id=None):
        '''
        Get question by id
        '''

        if not Question.objects.filter(id=id).exists():
             return Response(status=status.HTTP_404_NOT_FOUND) 

        question = Question.objects.get(id=id)
        serializer = QuestionSerializer(question)
        serializer.data['answers'] = json.loads(serializer.data['answers'])
        return Response(serializer.data, status=status.HTTP_200_OK)


    def destroy(self, request, id=None):
        '''
        Delete a question
        '''

        if Question.objects.filter(id=id).exists():
            questions = Question.objects.filter(id=id)
            questions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)