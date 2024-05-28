from django.urls import path, include
from rest_framework import routers

from .views import CompositionModelViewSet, RatingCreateAPIView, CommentModelViewSet


app_name = 'compositions'


router = routers.DefaultRouter()
router.register(r'compositions', CompositionModelViewSet)
router.register(r'comments', CommentModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('ratings/', RatingCreateAPIView.as_view()),
]
