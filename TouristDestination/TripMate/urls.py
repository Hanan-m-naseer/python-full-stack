# TripMate/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TripMate_app.urls')),         # Frontend (HTML templates)
    path('api/', include('TripMate_app.api_urls')), # API (ViewSets)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
