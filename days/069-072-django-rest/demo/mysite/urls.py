from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view

TITLE = 'Quotes API'

schema_view = get_schema_view(title=TITLE)

urlpatterns = [
    path('', include('quotes.urls')),
    path('my-backend/', admin.site.urls),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('schema/', schema_view),
]
