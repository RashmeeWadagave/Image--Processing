from django.contrib import admin
from django.urls import path
from MyApi.views import Home,MyFirstAPI
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",Home),
    path("api/v1/",MyFirstAPI)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
