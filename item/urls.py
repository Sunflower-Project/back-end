from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'item', ItemViewSet, basename='item')
router.register(r'comment', CommentViewSet, basename='comment')
urlpatterns = router.urls
