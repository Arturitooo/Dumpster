from .views import ProjectViewset
from rest_framework.routers import DefaultRouter

# Create your urls here.

router = DefaultRouter()
router.register("project", ProjectViewset, basename="project")
urlpatterns = router.urls
