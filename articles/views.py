from django.shortcuts import render
from django.views.generic import ListView,DetailView
from app.utils import common_data
from .models import Categories,Products
class ProjectDetailView(DetailView):
    model = Products
    template_name = 'post.html'
    context_object_name = 'article'
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView,self).get_context_data(**kwargs)
        context.update(common_data())
        context['title']='Interior Designer Portfolio'
        return context