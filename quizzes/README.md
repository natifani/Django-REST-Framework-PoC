# PoC for Django REST Framework

This repository contains a proof of concept project built with Django REST Framework. The purpose of this project is to demonstrate the capabilities of the framework and provide a basic overview of them for learning purposes.

The project showcases an app consisting of REST APIs for managing data related to quizzes.

The application implements APIs for 3 main entities: categories, quizzes and questions. The categories define different quiz topics (art, music, sciences, etc.). The quizzes contain basic information, such as description, creation time, points, and are in one-to-many relationship with the categories. The questions describe actual quiz questions (modelled as one-to-many relationship) and answers, marking the correct and incorrect ones accordingly. 


## Basic Concepts

The Django REST Framework is a powerful toolset for creating Web APIs constructed on top of the well-known Python web framework Django. It provides a variety of features and tools that make it simple to create APIs, including serialization, authentication, routing, etc.

This PoC provides a basic overview of the following concepts:

### Serialization

In Django REST Framework, serializers are responsible for the conversion between model instances and JSON/XML formats that are easily understandable by front-end applications. During deserialization, the incoming data is also validated.

The project demonstrates the usefulness of serializers through the use of the `ModelSerializer`,  which automatically generates fields based on the model's fields, making it easy to map between model instances and JSON/XML representations. An example for the serialization of the quiz category model:

```
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category"]
```

### Viewsets

Viewsets in Django Rest Framework are class-based views, which simplify the management of API code by enabling multiple actions for a single resource and grouping related views together. They provide a built-in support for the common CRUD operations for a resource, implementing actions like listing, retrieving by id, creating, updating and deleting each corresponding to specific HTTP methods according to the conventions.

The PoC implements three `ViewSet` classes for categories, quizzes and questions separately each mapped to different URL endpoints.

### Routing

Routing refers to the process of mapping URLs to views and viewsets, or other URLs. The URL routing can be defined in separate `urls.py` files in the project. 

- *urls.py* file of the project:
```
urlpatterns = [
    ...
    path('api/', include('quizzes_api.urls'))
]
```

- *urls.py* file of the application:
```
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
```
The router then examines the viewset's methods and instantly creates the correct URL patterns for each operation in accordance with the RESTful convetions.

### Authentication

The framework offers a number of authentication methods, and it also has an extensive permission system that can limit access to particular resources based on different criteria.

Within the project, two different authentication methods are included:
-   *token-based authentication*, which uses a simple token-based HTTP Authentication scheme
-   *session-based authentication*, which uses Django's default session backend

The determination whether a request should be granted or denied access is executed at the beginning of the view, before any other code is allowed to proceed.  

In the case of the PoC, the `IsAuthenticatedOrReadOnly` permission class is used, which allows only read-only access to unauthenticated users.

## Commands

The project was initialized with the following command:
```
django-admin startproject quizzes
```

The app within the project was created with the following command:
```
python manage.py startapp quizzes_api
```

After cloning the repository, first you need to apply the database migrations.

To propagate changes made on the models into the database schema:
```
python manage.py makemigrations
python manage.py migrate
```

After this, the application can be started. To launch the development server:
```
python manage.py runserver
```

Once the server is running, you can access the API endpoints with tools such as curl, Postman, or the UI in a web browser provided by the framework.
