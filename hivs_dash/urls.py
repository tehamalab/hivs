from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('reports', views.ReportsView.as_view(), name='reports'),
]
