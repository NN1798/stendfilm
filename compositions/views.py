from django.shortcuts import render
from django.views.generic import ListView

from .models import Composition


class CompositionListView(ListView):
    model = Composition
    template_name = 'compositions/index.html'
