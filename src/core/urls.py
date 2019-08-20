from rest_framework.routers import DefaultRouter

from core.apiviews import UserViewSet


version = 'v1'
router = DefaultRouter()
router.register(f'{version}/users', UserViewSet, base_name='users')

urlpatterns = router.urls
