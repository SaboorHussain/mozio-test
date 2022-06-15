from django.urls import path
from . import views

urlpatterns = [

    #### Providers ####
    path('providers/create/', views.providerCreate.as_view(), name='create-provider'),
    path('providers/list/', views.providerList.as_view(), name='list-providers'),
    path('providers/update/<str:pk>/',
         views.providerUpdate.as_view(), name='update-provider'),
    path('providers/delete/<str:pk>/',
         views.providerDelete.as_view(), name='delete-provider'),



    #### ServiceAreas ####
    path('service-areas/create/', views.serviceAreaCreate.as_view(),
         name='create-service-area'),
    path('service-areas/list/', views.serviceAreaList.as_view(),
         name='list-service-areas'),
    path('service-areas/update/<str:pk>/',
         views.serviceAreaUpdate.as_view(), name='update-service-area'),
    path('service-areas/delete/<str:pk>/',
         views.serviceAreaDelete.as_view(), name='delete-service-area'),


    path('polygons/polygon-list-by-latlong/', views.polygonListByLatLong.as_view(),
         name='polygon-list-by-latlong')
]
