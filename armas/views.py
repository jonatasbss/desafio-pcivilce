from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import ArmaSerializer, MunicaoSerializer
from .models import Arma, Municao


# Create your views here.
class ArmamentoViewSet(viewsets.ModelViewSet):
    serializer_class = ArmaSerializer
    queryset = Arma.objects.all()


class MunicaoViewSet(viewsets.ModelViewSet):
    serializer_class = MunicaoSerializer
    queryset = Municao.objects.all()
