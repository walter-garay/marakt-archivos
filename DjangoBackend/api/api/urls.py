from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from archivos import views
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()

router.register('usuarios', views.UsuarioViewSet)
router.register('archivos', views.ArchivoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='api/'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
