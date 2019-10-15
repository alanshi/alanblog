
from django.urls import path

from app.blog import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('view/<int:pk>', views.Detail.as_view(), name='article_details'),
    
]
