from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from apps.menuapp.models import Menu, Option
from datetime import date
# Create your tests here.


class HomePageTest(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'menuapp/home.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h5>Welcome to NoraApp</h5>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')


class LoginPageTest(SimpleTestCase):

    def test_login_page_status_code(self):
        response = self.client.get('/accounts/login/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'menuapp/login.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/accounts/login/')
        self.assertContains(response, '<h5>Login</h5>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/accounts/login/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')


class LogoutPageTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='usertest', password='1234')
        self.client_logged = Client()
        self.client_logged.force_login(user)

        self.client_unlogged = Client()

    def test_logout_logged(self):
        response = self.client_logged.get('/accounts/logout/')
        self.assertEquals(response.status_code, 200)

    def test_logout_unlogged(self):
        response = self.client_unlogged.get('/accounts/logout/')
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/')


class AccessMenuItemsPage(TestCase):

    def setUp(self):
        user = User.objects.create(username='usertest', password='1234')
        self.client_logged = Client()
        self.client_logged.force_login(user)

        self.client_unlogged = Client()

        dateTest = str(date.today())
        self.menu = Menu.objects.create(title_menu='Menu Test', menu_date=dateTest)
        self.menu_id = str(self.menu.id)

    def test_access_page_menu_list_unlogged_user(self):
        response = self.client_unlogged.get('/menu/list')
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/menu/list')

    def test_access_page_menu_list_logged_user(self):
        response = self.client_logged.get('/menu/list')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'menuapp/menu_list.html')

    def test_access_page_menu_create_unlogged_user(self):
        response = self.client_unlogged.get('/menu/create')
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/menu/create')

    def test_access_page_menu_create_logged(self):
        response = self.client_logged.get('/menu/create')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('menuapp/menu_create.html')

    def test_access_page_menu_detail_logged(self):
        response = self.client_logged.get(f'/menu/{self.menu_id}')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('menuapp/menu_detail.html')

    def test_access_page_menu_detail_unlogged(self):
        response = self.client_unlogged.get(f'/menu/{self.menu_id}')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('menuapp/menu_detail.html')

    def test_access_menu_delete_logged(self):
        response = self.client_logged.get(f'/menu/{self.menu_id}/delete')
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/menu/list')

    def test_access_menu_delete_unlogged(self):
        response = self.client_unlogged.get(f'/menu/{self.menu_id}/delete')
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next=/menu/{self.menu_id}/delete')


class AccessOptionItemsPage(TestCase):

    def setUp(self):
        user = User.objects.create(username='usertest', password='1234')
        self.client_logged = Client()
        self.client_logged.force_login(user)

        self.client_unlogged = Client()

        dateTest = str(date.today())
        self.menu = Menu.objects.create(title_menu='Menu Test', menu_date=dateTest)
        self.menu_id = str(self.menu.id)

        self.option = Option.objects.create(title_option='Option Test', menu=self.menu)
        self.option_id = str(self.option.id)

    def test_access_page_option_create_logged(self):
        response = self.client_logged.get(f'/menu/{self.menu_id}/option/create')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('menuapp/option_add.html')

    def test_access_page_option_create_unlogged(self):
        response = self.client_unlogged.get(f'/menu/{self.menu_id}/option/create')
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next=/menu/{self.menu.id}/option/create')

    def test_access_page_option_edit_logged(self):
        response = self.client_logged.get(f'/menu/{self.menu_id}/option/edit/{self.option_id}')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('menuapp/option_create.html')

    def test_access_page_option_edit_unlogged(self):
        response = self.client_unlogged.get(f'/menu/{self.menu_id}/option/edit/{self.option_id}')
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next=/menu/{self.menu_id}/option/edit/{self.option_id}')

    def test_access_page_option_delete_logged(self):
        response = self.client_logged.get(f'/menu/{self.menu_id}/option/delete/{self.option_id}')
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, f'/menu/{self.menu_id}')

    def test_access_page_option_delete_unlogged(self):
        response = self.client_unlogged.get(f'/menu/{self.menu_id}/option/delete/{self.option_id}')
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next=/menu/{self.menu_id}/option/delete/{self.option_id}')


class AccessOrderItemsPage(TestCase):

    def setUp(self):
        user = User.objects.create(username='usertest', password='1234')
        self.client_logged = Client()
        self.client_logged.force_login(user)

        self.client_unlogged = Client()

        dateTest = str(date.today())
        self.menu = Menu.objects.create(title_menu='Menu Test', menu_date=dateTest)
        self.menu_id = str(self.menu.id)

    def test_access_page_order_list_unlogged_user(self):
        response = self.client_unlogged.get('/order/list')
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/order/list')

    def test_access_page_order_list_logged_user(self):
        response = self.client_logged.get('/order/list')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'menuapp/order_list.html')

    def test_access_order_logged(self):
        response = self.client_logged.get(f'/order/create/{self.menu_id}/order/')
        self.assertEquals(response.status_code, 200)

    def test_access_order_unlogged(self):
        response = self.client_unlogged.get(f'/order/create/{self.menu_id}/order/')
        self.assertEquals(response.status_code, 200)
