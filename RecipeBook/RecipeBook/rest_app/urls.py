from django.urls import path
from .views import RecipeCreateView, RecipeListView, RecipeUpdateView, RecipeDeleteView
urlpatterns = [
    path('create/', RecipeCreateView.as_view(), name='create-recipe'),
    path('detail', RecipeListView.as_view(), name='detail'),
    path('update/<int:pk>/', RecipeUpdateView.as_view(), name='update-recipe'),
    path('delete/<int:pk>/', RecipeDeleteView.as_view(), name='delete-recipe'),
]