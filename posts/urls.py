from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

post_list = PostView.as_view({
    'post': 'create',
    'get': 'list'
})
post_detail = PostView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

router = routers.DefaultRouter()
router.register(r'', PostView)

# urlpatterns = format_suffix_patterns([
#     path('', post_list, name='post_list'),
#     path('/<int:pk>/', post_detail, name='post_detail'),
# ])

urlpatterns = [
    path('', include(router.urls)),
]