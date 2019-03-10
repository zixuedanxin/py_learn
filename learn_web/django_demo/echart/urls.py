from django.conf.urls import url
from . import views

app_name = 'echart'
urlpatterns = [
   url(r'^pyechart3d/$', views.pyechart3d, name='echart'),
]