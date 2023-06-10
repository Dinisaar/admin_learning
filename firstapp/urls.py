from django.urls import include
from django.urls import re_path as url
from . import views
from django.urls import path

# urlpatterns = [
#     re_path('', views.index, name='index'),
#     re_path(r'^course/$', views.courseListView.as_view(), name='course'),
#     re_path(r'^course/(?P<pk>\d+)$', views.courseDetailView.as_view(), name='данные о курсе')
# ]


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^course/$', views.courseListView.as_view(), name='course'),
    url(r'^course/(?P<pk>\d+)$', views.courseDetailView.as_view(), name='данные о курсе')
]


