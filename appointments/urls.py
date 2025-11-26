from django.urls import path
from .views import AppointmentListCreate, AppointmentDetail

urlpatterns = [
    path('', AppointmentListCreate.as_view(), name='appointment-list'),
    path('<int:pk>/', AppointmentDetail.as_view(), name='appointment-detail'),
]