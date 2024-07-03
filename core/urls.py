from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from upload.views import image_upload, my_json_view


urlpatterns = [
    path("", image_upload, name="upload"),
    path("live/", my_json_view, name="my_json_view"),
    # path("counter/", counter, name="counter"),
    path("admin/", admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
