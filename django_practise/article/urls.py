from django.urls import path, include

urlpatterns = [
    path('', include("article.api.urls", namespace="articles")),
]
