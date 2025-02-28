from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include

from app.settings import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include("authentication.urls")),
    path('api/products/', include("products.urls")),
]
if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()