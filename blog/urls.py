from django.urls import path
from django.views.generic import CreateView
from .views import ImageList, ImageDetail
urlpatterns = [
    path('image/', ImageList.as_view()),
    path('image/<int:pk>/', ImageDetail.as_view()),
]

