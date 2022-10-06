from django.contrib import admin
from django.urls import include, path
from api_about import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'resume', views.ResumeViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
