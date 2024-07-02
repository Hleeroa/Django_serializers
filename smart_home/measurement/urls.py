from django.urls import path
from measurement.views import SensorPost, SensorPut, MeasurementPost

urlpatterns = [
    path('sensors/', SensorPost.as_view()),
    path('sensors/<pk>/', SensorPut.as_view()),
    path('measurements/', MeasurementPost.as_view())
]
