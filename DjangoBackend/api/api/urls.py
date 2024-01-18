from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from archivos import views
from django.views.generic import RedirectView


router = DefaultRouter()

router.register('usuarios', views.UsuarioViewSet)
router.register('archivos', views.ArchivoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='api/'))
]