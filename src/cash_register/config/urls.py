from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import URLPattern, URLResolver, include, path


urlpatterns: list[URLPattern | URLResolver] = [
    path("admin/", admin.site.urls),
    path("", include("cash_register.checks.urls", namespace="checks")),
    path("", include("cash_register.items.urls", namespace="items")),
    path("", include("cash_register.monitoring.urls", namespace="monitoring")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += [
        path("api-auth/", include("rest_framework.urls", namespace="drf")),
    ]
