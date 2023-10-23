from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Product, Category


class IndexView(TemplateView):
    template_name = 'products/index.html'


class CategoryListView(ListView):
    model = Category

