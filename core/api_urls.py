from rest_framework.routers import DefaultRouter
from .api_views import ServicioViewSet, ContactoViewSet

router = DefaultRouter()
router.register(r'servicios', ServicioViewSet, basename='servicio')
router.register(r'contactos', ContactoViewSet, basename='contacto')

urlpatterns = router.urls
