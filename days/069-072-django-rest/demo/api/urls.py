from django.urls import path

from .views import QuoteList, QuoteDetail

urlpatterns = [
    path('<int:pk>/', QuoteDetail.as_view()),
    path('', QuoteList.as_view()),
]
