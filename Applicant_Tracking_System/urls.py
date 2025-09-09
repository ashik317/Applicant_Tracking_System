from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Schema + Docs
    # Schema JSON
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Swagger UI
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    # ReDoc
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
