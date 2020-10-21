import os
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

adminURL = ''
base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, "..", "..", "..", "admin.txt"))
with open(file_path, "r") as f:
    adminURL = f.read().strip()

urlpatterns = [
    path('', include('blog.urls')),
    path(adminURL, admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
