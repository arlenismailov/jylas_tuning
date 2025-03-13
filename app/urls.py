from django.urls import path
from .views import (
    SpoilerViewSet, ColorViewSet, TintingViewSet, RestylingViewSet, BrandViewSet, 
    BumperViewSet, RearBumperViewSet, SideSkirtViewSet, DiscsViewSet, CarModelViewSet,
    save_car, get_car  # Добавляем импорт новых функций
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'spoilers', SpoilerViewSet)
router.register(r'colors', ColorViewSet)
router.register(r'tintings', TintingViewSet)
router.register(r'restyling', RestylingViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'bumpers', BumperViewSet)
router.register(r'rear_bumpers', RearBumperViewSet)
router.register(r'side_skirts', SideSkirtViewSet)
router.register(r'discs', DiscsViewSet)
router.register(r'car_models', CarModelViewSet)

urlpatterns = router.urls

# Добавляем новые URL-маршруты к уже существующим
urlpatterns += [
    path('car/save/', save_car, name='save_car'),
    path('car/<uuid:uuid>/', get_car, name='get_car'),
]