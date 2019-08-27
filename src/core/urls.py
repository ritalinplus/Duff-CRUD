from rest_framework.routers import DefaultRouter

from core.apiviews import ClientViewSet


version = 'v1'
router = DefaultRouter()
router.register(f'{version}/clients', ClientViewSet, base_name='clients')

urlpatterns = router.urls
