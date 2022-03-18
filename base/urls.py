from django.urls import path, include
from . import views
from base.views import MemberViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'member', MemberViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]