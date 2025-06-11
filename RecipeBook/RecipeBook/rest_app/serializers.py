from . models import *
from rest_framework import serializers

class RecipeSerializers(serializers.ModelSerializer):
    Recipe_img=serializers.ImageField (required=False)

    class Meta:
        model = Recipes
        field = '__all__'