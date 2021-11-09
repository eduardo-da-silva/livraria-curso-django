from django.db import models
from django.db.models import F
from django.contrib.auth.models import User


class Categoria(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao


class Editora(models.Model):
    nome = models.CharField(max_length=255)
    site = models.URLField()

    def __str__(self):
        return self.nome


class Autor(models.Model):
    class Meta:
        verbose_name_plural = "autores"

    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=32)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )
    autores = models.ManyToManyField(Autor, related_name="livros")

    def __str__(self):
        return "%s (%s)" % (self.titulo, self.editora)


class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZADO = 2, "Realizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(
        choices=StatusCompra.choices, default=StatusCompra.CARRINHO
    )

    @property
    def total(self):
        queryset = self.itens.all().aggregate(
            total=models.Sum(F("quantidade") * F("livro__preco"))
        )
        return queryset["total"]


class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField()
