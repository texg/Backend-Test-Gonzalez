from django.test import TestCase
from apps.menuapp.models import Menu, Option, Order
from datetime import date
# Create your tests here.


class MenuModelTest(TestCase):

    def setUp(self):
        dateTest = str(date.today())
        Menu.objects.create(title_menu='Menu Test', menu_date=dateTest)

    def test_menu_was_created(self):
        menu = Menu.objects.get(title_menu='Menu Test')
        field = menu.title_menu
        self.assertEquals(field, 'Menu Test')

    def test_title_menu_label(self):
        menu_id = Menu.objects.first().id
        menu = Menu.objects.get(id=menu_id)
        field_label = menu._meta.get_field('title_menu').verbose_name
        self.assertEquals(field_label, 'title menu')

    def test_menu_date_label(self):
        menu_id = Menu.objects.first().id
        menu = Menu.objects.get(id=menu_id)
        field_label = menu._meta.get_field('menu_date').verbose_name
        self.assertEquals(field_label, 'menu date')


class OptionModelTest(TestCase):

    def setUp(self):
        dateTest = str(date.today())
        Menu.objects.create(title_menu='Menu Test', menu_date=dateTest)
        Option.objects.create(title_option='Ensalada Test', menu=Menu.objects.first())

    def test_option_was_created(self):
        option = Option.objects.get(title_option='Ensalada Test')
        field = option.title_option
        self.assertEquals(field, 'Ensalada Test')

    def test_title_option(self):
        option_id = Option.objects.first().id
        option = Option.objects.get(id=option_id)
        field_label = option._meta.get_field('title_option').verbose_name
        self.assertEquals(field_label, 'title option')


class OrderModelTest(TestCase):

    def setUp(self):
        dateTest = str(date.today())
        Menu.objects.create(title_menu='Menu Test', menu_date=dateTest)
        menu_id = Menu.objects.first()
        Option.objects.create(title_option='Ensalada Test', menu=menu_id)
        option_id = Option.objects.first()
        Order.objects.create(email_worker='test@test.cl', name_worker='test',
                             option_selected=option_id, comment='any comment')

    def test_order_was_created(self):
        option = Order.objects.get(name_worker='test')
        field = option.name_worker
        self.assertEquals(field, 'test')

    def test_email_worker_field(self):
        order_id = Order.objects.first().id
        order = Order.objects.get(id=order_id)
        field_label = order._meta.get_field('email_worker').verbose_name
        self.assertEquals(field_label, 'email worker')

    def test_name_worker_field(self):
        order_id = Order.objects.first().id
        order = Order.objects.get(id=order_id)
        field_label = order._meta.get_field('name_worker').verbose_name
        self.assertEquals(field_label, 'name worker')

    def test_option_selected_field(self):
        order_id = Order.objects.first().id
        order = Order.objects.get(id=order_id)
        field_label = order._meta.get_field('option_selected').verbose_name
        self.assertEquals(field_label, 'option selected')

    def test_comment_field(self):
        order_id = Order.objects.first().id
        order = Order.objects.get(id=order_id)
        field_label = order._meta.get_field('comment').verbose_name
        self.assertEquals(field_label, 'comment')
