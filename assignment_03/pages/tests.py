from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

# Create your tests here.
class RegistrationTestCase(TestCase):
    username = "newuser"
    email = "newuser@email.com"


    def test_signup_page_status_code(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)


    def test_login_page_status_code(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)


    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, new_user.username)
        self.assertEqual(get_user_model().objects.all()[0].email, new_user.email)


    def test_search_bar(self):
        search_request = "text"
        new_user = get_user_model().objects.create_user(
            self.username, self.email
        )
        Post.objects.create(title="title_name", author=new_user, body="body_text")
        response = self.client.post("/search/",{"searched_data":"title"})
        search_result = Post.objects.filter(body__contains = search_request)
        self.assertEqual(Post.objects.all().count(), len(response.context['searched_results']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(search_result[0].title, response.context['searched_results'][0].title)
        self.assertEqual(search_result[0].body, response.context['searched_results'][0].body)
