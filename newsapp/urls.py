from django.urls import path,include

from newsapp.views import CategoryAPIView , NewsAPIView , AuthorAPIView

urlpatterns =[
    path('categories/', CategoryAPIView.as_view(), name='Categories'),
    path('news/', NewsAPIView.as_view(), name='News'),
    path('authors/', AuthorAPIView.as_view(), name='Authors'),
]