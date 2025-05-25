from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi


from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/account/', include("account.urls")),
    path('api/book/', include("book.urls")),
    path('api/author/', include("author.urls")),
    path('api/performer/', include("performer.urls")),
    path('api/category/', include("category.urls")),
    path('api/order/', include("order.urls")),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),





]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)