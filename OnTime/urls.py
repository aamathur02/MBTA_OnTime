from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.TripListView.as_view(), name = 'trip_changelist'),
    path('add/', views.TripCreateView.as_view(), name = 'trip_add'),
    path('<int:pk>/', views.TripUpdateView.as_view(),name = 'trip_change'),

    path('ajax/load-stops/', views.load_stops, name='ajax_load_stops'),  # <-- this one here

]