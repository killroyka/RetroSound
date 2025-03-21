from rest_framework.routers import DefaultRouter

from .views import ProductView, ProductImageView, GenreView

router = DefaultRouter()
router.register('images', ProductImageView)
router.register('genres', GenreView)
router.register('', ProductView)
urlpatterns = [
              ] + router.urls
