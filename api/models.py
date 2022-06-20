from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Choices(models.Model):
    name = models.CharField(max_length=255, verbose_name="nom")

    def __str__(self):
        return self.name


class Genre(Choices):
    pass


class Platform(Choices):
    pass


class Support(Choices):
    pass


class Developer(Choices):
    pass


class Editor(Choices):
    pass


class Game(models.Model):
    name = models.CharField(max_length=255, verbose_name="nom")
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre, verbose_name="genres")
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE, verbose_name="editeur")
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, verbose_name="développeur")


class Edition(models.Model):
    name = models.CharField(max_length=255, verbose_name="nom")
    isDLC = models.BooleanField(verbose_name="est un dlc")
    price = models.FloatField(verbose_name="prix réduit(vrai prix)")
    initial_price = models.FloatField(verbose_name="prix initial")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="jeu", related_name="editions")
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, verbose_name="plateforme")

    def __str__(self):
        return f"{self.name} -"

class Key(models.Model):
    code = models.CharField(max_length=255, verbose_name="code")
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE, verbose_name="édition")


class DiscountCode(models.Model):
    code = models.CharField(max_length=255)
    discount = models.FloatField(verbose_name="réduction(%)")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="date de création")


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="utilisateur")
    editions = models.ManyToManyField(Edition, verbose_name="éditions")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="date de création")
    code = models.ForeignKey(DiscountCode, on_delete=models.CASCADE, verbose_name="code")
