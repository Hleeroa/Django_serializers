from rest_framework import serializers
from measurement.models import Sensor, Measurements

# TODO: опишите необходимые сериализаторы


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = ['id', 'sensor', 'temperature', 'image']



class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = ['temperature', 'created_at']


class SensorSerializer(serializers.ModelSerializer):
    measurement = MeasurementsSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurement']
