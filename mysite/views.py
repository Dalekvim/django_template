from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
  template_name = "mysite/home.html"

  extra_context = {
    'title': 'Home',
    'heading': 'Home Page',
  }

class AboutView(TemplateView):
  template_name = "mysite/about.html"

  extra_context = {
    'title': 'About',
    'heading': 'About Page',
  }