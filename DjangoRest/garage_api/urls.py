from django.urls import path

from garage_api.views import CarsListApiView, CarDetailApiView, manufacturers_list_view, manufacturer_details_view

urlpatterns = [
    path('cars/', CarsListApiView.as_view()),
    path('car/<int:pk>/', CarDetailApiView.as_view()),
    path('manufacturers/', manufacturers_list_view),
    path('manufacturer/<int:pk>/', manufacturer_details_view),
]