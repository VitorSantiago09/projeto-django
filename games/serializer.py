from rest_framework import serializers
from games.models import Category


#CategorySerializer nome generico
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        #__all__ adiciona todos os campos dentro do serializer ao inves de ter que digitar um por um
        fields = '__all__'
