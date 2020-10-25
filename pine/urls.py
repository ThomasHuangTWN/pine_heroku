from django.contrib import admin
from django.urls import include, path
from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('library.urls')),
    path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# django does not serve static by default