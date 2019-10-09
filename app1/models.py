from django.db import models

TIPO = (
    (1, 'despesa'),
    (2, 'receita')
    )


class Emissor(models.Model):

    cpnj = models.CharField('CNPJ', max_length=50, primary_key=True)
    nome = models.CharField('nome', max_length=50)

    def __str__(self):

        return str(self.cnpj)


class Lancamento(models.Model):

    num_nota_fiscal = models.CharField('numero da nota fiscal', max_length=50, blank=True, null=True)
    receita_despesa = models.PositiveSmallIntegerField('receita ou despesa', choices=TIPO)  # True = Receita
    #centro_custo = models.ForeignKey(CentroCusto, blank=False, null=False, on_delete=models.CASCADE)
    emissor = models.ForeignKey(Emissor, blank=True, null=True, on_delete=models.CASCADE)
    # projeto = models.ForeignKey(Projeto, blank=True, null=True, on_delete=models.CASCADE)
    valor_nota = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    desconto = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    valor_total = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)

    class Meta:
        verbose_name = 'Lançamento'
        verbose_name_plural = 'Lançamentos'

    def __str__(self):

        return str(self.pk)