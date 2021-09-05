from django.urls import include, path
from rest_framework import routers

from forest import views, seeder, analytics

router = routers.DefaultRouter()
router.register(r'forest', views.ForestViewSet)
router.register(r'trees', views.TreeViewSet)
router.register(r'events', views.EventViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('seeds', seeder.seeds),
    path('analytics', analytics.get_frame),
]