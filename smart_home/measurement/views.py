# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from measurement.models import Sensor, Measurements
from measurement.serializers import SensorSerializer, MeasurementsSerializer, MeasurementSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


class SensorPost(ListCreateAPIView):
    queryset = Sensor.objects.all().order_by('id')
    serializer_class = SensorSerializer


class SensorPut(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementPost(ListCreateAPIView):
    queryset = Measurements.objects.all().order_by('id')
    serializer_class = MeasurementSerializer
