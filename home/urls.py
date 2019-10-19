from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('miners_pages.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/', include('miners_account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
