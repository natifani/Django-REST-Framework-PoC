from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from quizzes_api.models import Category
from quizzes_api.serializers import CategorySerializer, CategoryNestedSerializer

class CategoryViewSet(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        '''
        List all the categories
        '''

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        '''
        Create a category
        '''
       
        data = {
            "category": request.data.get("category"), 
        }

        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, id=None):
        '''
        Get category by id
        '''

        if not Category.objects.filter(id=id).exists():
             return Response(status=status.HTTP_404_NOT_FOUND) 

        category = Category.objects.get(id=id)
        serializer = CategoryNestedSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
    def destroy(self, request, id=None):
        '''
        Delete category
        '''

        if Category.objects.filter(id=id).exists():
            category = Category.objects.get(id=id)
            category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
