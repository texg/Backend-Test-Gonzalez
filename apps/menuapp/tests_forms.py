from django.test import TestCase
import datetime
from apps.menuapp.forms import MenuCreate, OptionCreate, OrderCreate
# Create your tests here.


class MenuCreateFormTest(TestCase):

    def test_menu_create_form_title_menu_field(self):
        form = MenuCreate()
        self.assertTrue(form.fields['title_menu'].label == 'Title menu')

    def test_menu_create_form_date_not_valid(self):
        dateTest = datetime.date.today() - datetime.timedelta(days=1)
        form_data = {
            'title_menu': 'Form Test',
            'menu_date': dateTest
        }
        form = MenuCreate(data=form_data)
        self.assertFalse(form.is_valid())

    def test_menu_create_form_date_valid(self):
        dateTest = datetime.date.today()
        form_data = {
            'title_menu': 'Form Test',
            'menu_date': dateTest
        }
        form = MenuCreate(data=form_data)
        self.assertTrue(form.is_valid())


class OptionCreateFormTest(TestCase):

    def test_option_create_form_title_option_field(self):
        form = OptionCreate()
        self.assertTrue(form.fields['title_option'].label == 'Title option')

    def test_option_create_form_is_valid(self):
        form_data = {
            'title_option': 'Form Test',
            'menu': ''
        }
        form = OptionCreate(data=form_data)
        self.assertTrue(form.is_valid())


class OrderCreateFormTest(TestCase):

    def test_order_create_form_email_worker_field(self):
        form = OrderCreate()
        self.assertTrue(form.fields['email_worker'].label == 'Email worker')
        self.assertTrue(form.fields['name_worker'].label == 'Name worker')
        self.assertTrue(form.fields['option_selected'].label == 'Option selected')
        self.assertTrue(form.fields['comment'].label == 'Comment')

    def test_order_create_form_time_not_valid(self):
        dateTest = datetime.date.today() - datetime.timedelta(days=1)
        form_data = {
            'title_menu': 'Form Test',
            'menu_date': dateTest
        }
        form = MenuCreate(data=form_data)
        self.assertFalse(form.is_valid())

    def test_order_create_form_time_valid(self):
        dateTest = datetime.date.today()
        form_data = {
            'title_menu': 'Form Test',
            'menu_date': dateTest
        }
        form = MenuCreate(data=form_data)
        self.assertTrue(form.is_valid())
