from django.urls import path
from .views import home, pizzas, order, edit_order

urlpatterns=[
    path('', home, name='home'),
    path('list/', pizzas, name='list'),
    path('order/', order, name='order'),
    path('edit/<int:id>', edit_order, name='edit'),
    # path('delete/<int:id>', todo_delete, name='delete')


]