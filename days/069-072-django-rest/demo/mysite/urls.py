from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('quotes.urls')),
    path('my-backend/', admin.site.urls),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
