
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, LanguageViewSet, ProfileViewSet, ProjectViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
