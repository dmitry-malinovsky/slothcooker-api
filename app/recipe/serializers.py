from core.models import Tag, Ingredient, Recipe, Step

from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'calories', 'protein', 'carbohydrates', 'fats')
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'calories', 'protein', 'steps',
                  'carbohydrates', 'fats', 'tags', 'link')
        read_only_fields = ('id',)


class RecipeDetailSerializer(RecipeSerializer):
    tags = TagSerializer(many=True, read_only=True)


class StepSerializer(serializers.ModelSerializer):
    ingredient = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )

    class Meta:
        model = Step
        fields = ('id', 'action', 'ingredient',
                  'weight')
        read_only_fields = ('id',)
