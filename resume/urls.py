from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, about_me

urlpatterns = [
    path('', home),
    path('about', about_me),
    path('', include('contact.urls')),
    path('', include('projects.urls')),
    path('', include('order.urls')),
    path('', include('essay.urls')),
    path('', include('social_network.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
