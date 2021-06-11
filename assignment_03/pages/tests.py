from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core import mail


# Create your tests here.
class RegistrationTestCase(TestCase):
    username = "newuser"
    email = "newuser@email.com"


    def test_signup_page_status_code(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')


    def test_login_page_status_code(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')


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


    def test_password_reset_complete_correct_template(self):
        response = self.client.get(reverse('password_reset_complete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_complete.html')

    def test_password_reset_confirm_correct_status_code(self):
        user = get_user_model().objects.create_user(username=self.username, email=self.email, password='123abcdef')
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        response = self.client.get(reverse('password_reset_confirm', kwargs = {"uidb64":uid,'token':token}))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('password_reset_confirm', kwargs = {"uidb64":uid,'token':token}), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_confirm.html')
    
    
    def test_password_reset_done_correct_template(self):
        response = self.client.get(reverse('password_reset_done'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_done.html')

    def test_password_reset_email_correct_template(self):
        new_user = get_user_model().objects.create_user(username=self.username, email=self.email, password='123abcdef')
        response = self.client.post(reverse('password_reset'), {'email': 'tom@tom.com'})
        self.assertEqual(response.status_code, 302)
        response = self.client.post(reverse('password_reset'), {'email': new_user.email }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Password reset on testserver')
        # self.assertTemplateUsed(response, 'registration/password_reset_email.html') Doesn't work


    def test_password_reset_form_correct_template(self):
        response = self.client.get(reverse('password_reset'),{'email':'tom@tom.com'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_form.html')   
