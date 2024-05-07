from django.urls import path, include
from rest_framework import routers
from cliente import views

router = routers.DefaultRouter()
router.register(r'proyecto', views.ProgrammerViewSet)

urlpatterns = [
    path('', include(router.urls))
]