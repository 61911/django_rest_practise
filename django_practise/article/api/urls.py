from django.urls import path

from .views import ArticleView, ArticleGenericView, SingleArticleView

app_name = "articles"

urlpatterns = [
    # path('articles/', ArticleView.as_view()),
    path('articles/', ArticleGenericView.as_view()),
    path('articles/<int:pk>/', SingleArticleView.as_view()),
]
