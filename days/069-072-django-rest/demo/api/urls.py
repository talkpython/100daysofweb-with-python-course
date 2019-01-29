from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from .views import QuoteList, QuoteDetail

schema_view = get_swagger_view(title='PyBites Quotes API')

urlpatterns = [
    path('', QuoteList.as_view()),
    path('<int:pk>', QuoteDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('docs/', schema_view),
]
