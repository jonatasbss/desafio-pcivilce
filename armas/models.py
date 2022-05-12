from django.db import models


# Create your models here.
class Calibre(models.Model):
    desc_calibre = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        db_table = 'calibre'

    def __str__(self):
        return '{}'.format(self.desc_calibre)


class ObjetoTipo(models.Model):
    tipo_de_objeto = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        db_table = 'objeto_tipo'

    def __str__(self):
        return '{}'.format(self.tipo_de_objeto)


class Objeto(models.Model):
    objeto_tipo = models.ForeignKey('armas.ObjetoTipo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'objeto'

    def __str__(self):
        return '{}'.format(self.objeto_tipo)


class Arma(models.Model):
    marca_armamento = models.CharField(max_length=64, null=True, blank=True)
    modelo_armamento = models.CharField(max_length=64, null=True, blank=True)
    quantidade_de_tiros = models.IntegerField(null=True, blank=True)
    valor_estimado_armamento = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    imagem = models.CharField(max_length=128, null=True, blank=True)
    objeto_tipo = models.ForeignKey('armas.Objeto', related_name='arma', null=True, blank=True,
                                    on_delete=models.CASCADE)
    calibre = models.ForeignKey('armas.Calibre', related_name='calibre_arma', on_delete=models.CASCADE)

    class Meta:
        db_table = 'arma'
        ordering = ['marca_armamento']

    def __str__(self):
        return '{} - {}'.format(self.modelo_armamento, self.marca_armamento)

    """
    Alterando o metodo save() do models, é possivel, instanciar o objeto_tipo,
    que não é definido no inicio do preenchimento dos dados. Lembre-se de descomentar o
    metodo abaixo e comentar o metodo create do serializer, para obter os resultados.
    
    Fiz a definição para os dois modelos Arma e Munição.
    
    """

    def save(self, *args, **kwargs):
        if self.id is None:
            ot_arma, objt = ObjetoTipo.objects.get_or_create(tipo_de_objeto='arma')
            o, obj = Objeto.objects.get_or_create(objeto_tipo=ot_arma)
            o.save()
            self.objeto_tipo_id = o.id
        super(Arma, self).save(*args, **kwargs)


class Municao(models.Model):
    marca_municao = models.CharField(max_length=64, null=True, blank=True)
    modelo_municao = models.CharField(max_length=64, null=True, blank=True)
    valor_estimado_municao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    objeto_tipo = models.ForeignKey('armas.Objeto', related_name='municao', null=True, blank=True,
                                    on_delete=models.CASCADE)
    calibre = models.ForeignKey('armas.Calibre', related_name='calibre_municao', on_delete=models.CASCADE)

    class Meta:
        db_table = 'municao'
        ordering = ['marca_municao']

    def __str__(self):
        return '{} - {}'.format(self.modelo_municao, self.marca_municao)

    # def save(self, *args, **kwargs):
    #     if self.id is None:
    #         ot_municao, objt = ObjetoTipo.objects.get_or_create(tipo_de_objeto='municao')
    #         m, obj = Objeto.objects.get_or_create(objeto_tipo=ot_municao)
    #         m.save()
    #         self.objeto_tipo_id = m.id
    #     super(Municao, self).save(*args, **kwargs)
