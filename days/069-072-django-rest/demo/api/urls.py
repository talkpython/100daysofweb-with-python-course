from django.urls import path

from .views import QuoteAPIView

urlpatterns = [
    path('', QuoteAPIView.as_view()),
]
