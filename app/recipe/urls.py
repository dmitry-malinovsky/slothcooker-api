from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredient', views.IngredientViewSet)
router.register('recipes', views.RecipeViewSet)
router.register('step', views.StepViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
