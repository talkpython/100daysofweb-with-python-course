from django.urls import path

from . import views

app_name = 'quotes'
urlpatterns = [
    path('', views.quote_list, name='quote_list'),
    path('<int:pk>', views.quote_detail, name='quote_detail'),
    path('new', views.quote_new, name='quote_new'),
    path('edit/<int:pk>', views.quote_edit, name='quote_edit'),
    path('delete/<int:pk>', views.quote_delete, name='quote_delete'),
]
