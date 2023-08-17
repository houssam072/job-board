from django.urls import path, include
from . import views
from . import api


app_name = 'job'

urlpatterns = [
    path('',views.job_list, name='job_list'),
    path('add_jop', views.add_jop, name='add_jop'),
    path('<str:slug>',views.job_detailes, name='job_detail'),

    # api
    path('api/list', api.joblistapi, name='joblistapi'),
    path('api/list/<int:id>', api.job_detailes_api, name='job_detailes_api'),

]
