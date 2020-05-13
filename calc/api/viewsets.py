from rest_framework.viewsets import ModelViewSet
from calc.models import Calc
from .serializers import CalcSerializer


class CalcViewSet(ModelViewSet):
    queryset = Calc.objects.all()
    serializer_class = CalcSerializer

