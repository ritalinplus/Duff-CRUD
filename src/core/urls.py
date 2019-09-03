from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from core.apiviews import ClientViewSet


schema_view = get_swagger_view(title='Duff CRUD API')

version = 'v1'
router = DefaultRouter()
router.register(f'{version}/clients', ClientViewSet, base_name='clients')


urlpatterns = [
    path(f'{version}/swagger-docs/', schema_view)
]

urlpatterns += router.urls
