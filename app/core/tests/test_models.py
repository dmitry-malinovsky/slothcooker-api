from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@mail.com', password='123456'):
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_uset_with_correct_email(self):
        email = "myEmail@test.com"
        password = "124124"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_is_formatter(self):
        email = "myemail@TEST.com"
        password = "124124"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "12213")

    def test_super_user_is_created(self):
            user = get_user_model().objects.create_superuser(
                "myEmail@test.com",
                "124124"
            )

            self.assertTrue(user.is_superuser)
            self.assertTrue(user.is_staff)

    def test_tag_string(self):
        tag = models.Tag.objects.create(
           user=sample_user(),
           name='healthy'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_string(self):
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Carrot'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_string(self):
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Greek Salad'
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_step_string(self):
        step = models.Step.objects.create(
            user=sample_user(),
            action='Mix well'
        )

        self.assertEqual(str(step), step.action)
