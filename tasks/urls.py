from rest_framework import routers
from .views import TaskViewset

app_name='tasks'
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewset, basename="tasks")
urlpatterns = router.urls