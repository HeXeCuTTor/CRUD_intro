from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from measurements.models import Sensor, Measurement
from measurements.serializers import MeasurementSerializer, SensorDetailSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all() 
    serializer_class = SensorDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MeasurementsView(CreateAPIView):
    queryset = Measurement.objects.all() 
    serializer_class = MeasurementSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class SensorsFix(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all() 
    serializer_class = SensorDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    