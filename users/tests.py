from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve


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


class SignupTests(TestCase):
    username = "testuser"
    email = "testuser@gmail.com"

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, "hello there i am not in the page i guess")

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
