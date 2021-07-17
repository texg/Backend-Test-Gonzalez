from django.urls import path
from django.urls.resolvers import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path('menu', views.home, name="home"),
    path('menu/create', views.menu_create, name="menu_create"),
    path('menu/list', views.menu_list, name="menu_list"),
    path('menu/<pk>', views.menu_detail, name="menu_detail"),
    path('menu/<pk>/delete', views.menu_delete, name="menu_delete"),
    path('menu/<pk>/option/create', views.option_create, name="create_option"),
    path('menu/<menu_pk>/option/edit/<pk>', views.option_edit, name="edit_option"),
    path('menu/<menu_pk>/option/delete/<pk>', views.option_delete, name="delete_option"),
    path('order/list', views.order_list, name="order_list"),
    path('order/create/<menu_pk>/order/', views.order_create, name="order_create"),
]
