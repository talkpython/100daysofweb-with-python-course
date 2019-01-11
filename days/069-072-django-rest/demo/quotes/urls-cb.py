from django.urls import path

from . import views

app_name = 'quotes'
urlpatterns = [
    path('', views.QuoteList.as_view(), name='quote_list'),
    path('<int:pk>', views.QuoteView.as_view(), name='quote_detail'),
    path('new', views.QuoteCreate.as_view(), name='quote_new'),
    path('edit/<int:pk>', views.QuoteUpdate.as_view(), name='quote_edit'),
    path('delete/<int:pk>', views.QuoteDelete.as_view(), name='quote_delete'),
]
