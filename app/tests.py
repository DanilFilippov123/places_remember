from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from app.models import Place


# Create your tests here.

class TestWithOneUser(TestCase):
    UserModel = None
    user = None

    @classmethod
    def setUpTestData(cls):
        cls.UserModel = get_user_model()
        cls.user = cls.UserModel.objects.create_user(username='test', password='test', email='test@ya.ru')

    def setUp(self):
        self.client.logout()

    def user_login(self, password='test'):
        self.client.login(username=self.user.username, password=password)


class PlaceTest(TestWithOneUser):
    def tearDown(self):
        Place.objects.all().delete()

    def create_temp_place(self):
        return self.client.post(reverse("place_page"), {'name': 'name', 'comment': 'comment', 'lat': 2, 'lng': 2})

    def delete_temp_place(self, pk):
        return self.client.post(reverse("place_delete_page", kwargs={'pk': pk}))

    def one_user_create_place_another_user_act(self):
        user2 = self.UserModel.objects.create_user(username='test2', password='test2', email='test2@ya.ru')
        user1 = self.user

        self.user_login()
        self.create_temp_place()
        self.client.logout()
        self.assertEqual(user1.places.count(), 1)

        self.user = user2
        self.user_login('test2')

        return user1

    def test_logged_user_create_place(self):
        """
            Test creation of new place
        """
        self.user_login()
        resp = self.create_temp_place()
        self.assertRedirects(resp, reverse("my_places_page"))
        self.assertEqual(self.user.places.count(), 1)

    def test_anonymous_user_create_place(self):
        """
            Test that if user is not logged, redirect to login page
        """
        resp = self.create_temp_place()
        self.assertRedirects(resp, reverse("login_page") + f'?next={reverse("place_page")}')
        self.assertEqual(self.user.places.count(), 0)

    def test_create_and_delete_place(self):
        """
        Test user can delete his place
        """
        self.user_login()
        self.create_temp_place()
        place = self.user.places.get()
        self.delete_temp_place(place.pk)
        self.assertEqual(self.user.places.count(), 0)

    def test_delete_someone_else_place(self):
        """
        Test user can't delete someone else place
        """
        creator_user = self.one_user_create_place_another_user_act()
        resp = self.delete_temp_place(creator_user.places.get().pk)
        self.assertEqual(creator_user.places.count(), 1)
        self.assertEqual(resp.status_code, 403)

    def test_update_someone_else_place(self):
        """
        Test user can't update someone else place
        """
        creator_user = self.one_user_create_place_another_user_act()
        resp = self.client.post(reverse("place_update_page", kwargs={'pk': creator_user.places.get().pk}))
        self.assertEqual(resp.status_code, 403)


class UserTest(TestWithOneUser):

    def check_get_path_and_redirect_to_login(self, path_name, **kwargs):
        resp = self.client.get(reverse(path_name, kwargs=kwargs))
        self.assertRedirects(resp, reverse("login_page") + f'?next={reverse(path_name, kwargs=kwargs)}')

    def test_logged_user_redirect_to_places(self):
        """
        Test that if user is logged, redirect to his places
        """
        self.client.login(username='test', password='test')
        resp = self.client.get(reverse("hello_page"))
        self.assertRedirects(resp, reverse("my_places_page"))

    def test_anonymous_user_redirect_to_login(self):
        """
        Test that if user is not logged, redirect to login page
        """
        self.check_get_path_and_redirect_to_login('place_page')
        self.check_get_path_and_redirect_to_login('place_update_page', pk=0)
        self.check_get_path_and_redirect_to_login('my_places_page')
        self.check_get_path_and_redirect_to_login('place_page')

    def test_user_registration(self):
        """
        Test user registration - creation of UserProfile
        """
        resp = self.client.post(reverse("registration_page"),
                                {'username': 'test2', 'password1': 'tessakdknal@eq2eq209@)(t1', 'password2': 'tessakdknal@eq2eq209@)(t1'})
        self.assertEqual(self.UserModel.objects.count(), 2)
        new_user = self.UserModel.objects.get(username='test2')
        self.assertEqual(new_user.profile.user, new_user)
