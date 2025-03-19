from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Tuning API",
        default_version='v1',
        description="API documentation for tuning application",
        terms_of_service="https://www.google.com/policies/terms/",
         contact=openapi.Contact(email="contact@tuning.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
   )

urlpatterns = [
       path('admin/', admin.site.urls),
       path('api/', include('app.urls')),  # Убедитесь, что здесь нет циклических ссылок
       path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
       path('users/', include('users.urls')),   
       path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
