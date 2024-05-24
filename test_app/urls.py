from django.urls import path, include
from rest_framework.routers import DefaultRouter
from test_app.views import ItemViewSet

router = DefaultRouter()
router.register('', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
