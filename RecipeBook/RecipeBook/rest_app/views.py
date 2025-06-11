from django.shortcuts import render
from . models import Recipes
from rest_framework import generics
from . serializers import RecipeSerializers
from rest_framework.permissions import AllowAny
# Create your views here.

class RecipeCreateView(generics.CreateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializers
    permission_classes = [AllowAny ]  # Adjust permissions as needed

class RecipeListView(generics.RetrieveAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializers

class RecipeUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializers
    
class RecipeDeleteView(generics.DestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializers
   