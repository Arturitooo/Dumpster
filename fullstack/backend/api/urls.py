from .views import ProjectViewset, ProjectManagerViewset
from rest_framework.routers import DefaultRouter

# Create your urls here.

router = DefaultRouter()
router.register("project", ProjectViewset, basename="project")
router.register("projectmanager", ProjectManagerViewset, basename="projectmanager")
urlpatterns = router.urls
