from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import STP, Site, SubSite, Income, Beds
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

    def get_object(self, *args, **kwargs):
        return get_object_or_404(Site, nhs_code=self.kwargs['nhs_code'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the years for the income data
        income = Income.objects.filter(site=self.object.pk)
        income_years = [x.year for x in income]
        # get the years for the bed data
        beds = Beds.objects.filter(site=self.object.pk)
        bed_years = [x.year for x in beds]
        # add the years to the context
        context['income_years'] = income_years
        context['bed_years'] = bed_years
        return context


class STPDetail(DetailView):
    model = STP
    template_name = 'main/stp_detail.html'


class SubSiteDetail(DetailView):
    model = SubSite
    template_name = 'main/subsite_detail.html'

    def get_object(self, *args, **kwargs):
        return get_object_or_404(SubSite, nhs_code=self.kwargs['nhs_code'])
