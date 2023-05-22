from django.urls import path

from .views.categoryViewSet import CategoryViewSet
from .views.quizViewSet import QuizViewSet
from .views.questionViewSet import QuestionViewSet

urlpatterns = [
    path("categories", CategoryViewSet.as_view({
            'get': 'list',
            'post': 'create'
    })),
    path("categories/<int:id>", CategoryViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    })),
    path("quizzes", QuizViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path("quizzes/<int:id>", view=QuizViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    })),
    path("questions", QuestionViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path("questions/<int:id>", QuestionViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    })),
]