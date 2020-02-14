from django.urls import path
from .views import STPList, SiteList, SiteDetail, STPDetail, SubSiteDetail


app_name = 'main'

urlpatterns = [
    path('stp/', STPList.as_view(), name='stp_list'),
    path('site/', SiteList.as_view(), name='site_list'),
    path('sites/', SiteList.as_view(), name='sites_list'),
    path('site/<str:nhs_code>', SiteDetail.as_view(), name='site_detail'),
    path('stp/<str:slug>', STPDetail.as_view(), name='stp_detail'),
    path('site/<str:site>/<str:nhs_code>', SubSiteDetail.as_view(), name='subsite_detail'),
]
