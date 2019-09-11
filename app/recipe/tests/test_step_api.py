from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Ingredient, Step

from recipe.serializers import StepSerializer

STEPS_URL = reverse('recipe:step-list')


def sample_step(user, **params):
    defaults = {
        'action': 'Mix well'
    }
    defaults.update(params)

    return Step.objects.create(user=user, **defaults)


def sample_ingredient(user, name='Carrot'):
    return Ingredient.objects.create(user=user, name=name)


class PublicRecipeApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(STEPS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRecipeApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@test.com',
            'password123'
        )

        self.client.force_authenticate(self.user)

    def test_retrieve_steps(self):
        sample_step(self.user)
        sample_step(self.user)

        res = self.client.get(STEPS_URL)

        steps = Step.objects.all().order_by('-id')
        serializer = StepSerializer(steps, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_steps_limited_to_user(self):
        user2 = get_user_model().objects.create_user(
            'test_1@test.com',
            'password123'
        )

        sample_step(user=user2)
        sample_step(user=self.user)

        res = self.client.get(STEPS_URL)

        steps = Step.objects.filter(user=self.user)
        serializer = StepSerializer(steps, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data, serializer.data)

    def test_create_step(self):
        payload = {
            'action': 'Wait'
        }

        res = self.client.post(STEPS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        step = Step.objects.get(id=res.data['id'])

        for key in payload.keys():
            self.assertEqual(payload[key], getattr(step, key))

    def test_create_recipe_with_items(self):
        ingredient = sample_ingredient(user=self.user, name='Chicken')

        payload = {
            'action': 'Add',
            'ingredient': [ingredient.id],
            'weight': 100
        }

        res = self.client.post(STEPS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        step = Step.objects.get(id=res.data['id'])
        ingredients = step.ingredient.all()

        self.assertTrue(ingredients, ingredient)
