from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from todo.views import TodoViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
