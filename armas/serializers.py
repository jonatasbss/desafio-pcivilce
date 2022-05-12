from rest_framework import serializers
from .models import Arma, Municao, Objeto, ObjetoTipo


class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = '__all__'

    def create(self, validated_data):
        obj_tipo = ObjetoTipo.objects.get(tipo_de_objeto='arma')
        obj_arm = Objeto.objects.create(objeto_tipo=obj_tipo)
        validated_data['objeto_tipo'] = obj_arm
        armamento = super(ArmaSerializer, self).create(validated_data)

        return armamento


class MunicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municao
        fields = '__all__'

    def create(self, validated_data):
        obj_tipo = ObjetoTipo.objects.get(tipo_de_objeto='municao')
        obj_mun = Objeto.objects.create(objeto_tipo=obj_tipo)
        validated_data['objeto_tipo'] = obj_mun
        municao = super(MunicaoSerializer, self).create(validated_data)

        return municao
