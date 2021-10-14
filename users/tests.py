from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignUpPageView


class CustomTestUser(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='saifur',
            email='saifur@gmail.com',
            password='rahman'
        )

        self.assertEqual(user.username, 'saifur')
        self.assertEqual(user.email, 'saifur@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_super(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superemon',
            email='super@gmail.com',
            password='pass123'
        )
        self.assertEqual(admin_user.username, 'superemon')
        self.assertEqual(admin_user.email, 'super@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpPageTest(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, "hello there i am not in html template")

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignUpPageView.as_view().__name__
        )
