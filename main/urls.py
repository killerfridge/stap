from django.urls import path
from .views import STPList, SiteList, SiteDetail, STPDetail


app_name = 'main'

urlpatterns = [
    path('stp/', STPList.as_view(), name='stp_list'),
    path('site/', SiteList.as_view(), name='site_list'),
    path('sites/', SiteList.as_view(), name='sites_list'),
    path('site/<int:pk>', SiteDetail.as_view(), name='site_detail'),
    path('stp/<int:pk>', STPDetail.as_view(), name='stp_detail')
]
