from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('topfive', views.topfive, name='topfive'),
    path('northamerica', views.northamerica, name='northamerica'),
    path('southamerica', views.southamerica, name='southamerica'),
    path('africa', views.africa, name='africa'),
    path('europe', views.europe, name='europe'),
    path('asia', views.asia, name='asia'),
    path('australia', views.australia, name='australia'),
]