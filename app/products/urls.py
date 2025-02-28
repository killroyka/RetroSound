from rest_framework.routers import DefaultRouter

from .views import ProductView, ProductImageView

router = DefaultRouter()
router.register('images', ProductImageView)
router.register('', ProductView)
urlpatterns = [
              ] + router.urls
