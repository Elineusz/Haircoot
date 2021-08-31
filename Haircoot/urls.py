from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('reservation/', views.ReservationView.as_view(), name='reservation'),
    path('reservation/onetime/', views.ReservationOneTimeView.as_view(), name='reservation_one_time'),
    path('confirmed/', views.ReservationConfirmedView.as_view(), name='reservation_confirmed'),
    path('employee/', views.EmployeeView.as_view(), name='employee'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('policy/', views.PolicyView.as_view(), name='policy'),
    path('regulations/', views.RegulationsView.as_view(), name='regulation'),
    path('newservice/', views.NewserviceView.as_view(), name='newservice')
    ]
