from rest_framework.routers import SimpleRouter
from .viewsets import ReviewViewSet

router = SimpleRouter()
router.register('reviews', ReviewViewSet)
urlpatterns = router.urls