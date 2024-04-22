from django.urls import path

from .views import CompositionListView


app_name = 'compositions'


urlpatterns = [
    path('', CompositionListView.as_view()),
]
