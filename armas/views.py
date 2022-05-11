from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import ArmaSerializer, MunicaoSerializer
from .models import Arma, Municao


# Create your views here.
class ArmaAPIView(viewsets.ModelViewSet):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer

    def create(self, request, *args, **kwargs):
        serializer = ArmaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MunicaoAPIView(viewsets.ModelViewSet):
    queryset = Municao.objects.all()
    serializer_class = MunicaoSerializer
