from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import STP, Site
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
# Create your views here.


class STPList(ListView):
    model = STP
    template_name = 'main/stp_list.html'


class SiteList(ListView):
    model = Site
    template_name = 'main/site_list.html'


class SiteDetail(DetailView):
    model = Site
    template_name = 'main/site_detail.html'


class STPDetail(DetailView):
    model = STP
    template_name = 'main/stp_detail.html'