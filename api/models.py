from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have an username.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"


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
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField()
    default_edition = models.ForeignKey("Edition", on_delete=models.CASCADE, verbose_name="edition par défaut",
                                        null=True, blank=True, related_name="game_default")
    genres = models.ManyToManyField(Genre, verbose_name="genres")
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE, verbose_name="editeur")
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, verbose_name="développeur")

    def __str__(self):
        return f"{self.name}"


class Edition(models.Model):
    name = models.CharField(max_length=255, verbose_name="nom")
    isDLC = models.BooleanField(verbose_name="est un dlc", default=False)
    price = models.FloatField(verbose_name="prix réduit(vrai prix)")
    cover = models.ImageField(verbose_name="image de couverture")
    content = models.TextField(verbose_name="contenus", blank=True, null=True,
                               help_text="separate each content with '|' (AC Valhalla|AC Valhalla: Aube du Ranarok)")
    initial_price = models.FloatField(verbose_name="prix initial")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="jeu", related_name="editions")
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, verbose_name="plateforme")
    support = models.ForeignKey(Support, on_delete=models.CASCADE, verbose_name="support")

    def __str__(self):
        return f"{self.game} - {self.name} - {self.support}"


class Key(models.Model):
    code = models.CharField(max_length=255, verbose_name="code")
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE, verbose_name="édition", related_name="keys")

    def __str__(self):
        return f"{self.edition} - {self.code}"


class DiscountCode(models.Model):
    code = models.CharField(max_length=255)
    discount = models.FloatField(verbose_name="réduction(%)")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="date de création")

    def __str__(self):
        return f"${self.discount}"

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="utilisateur")
    editions = models.ManyToManyField(Edition, verbose_name="éditions")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="date de création")
    code = models.ForeignKey(DiscountCode, on_delete=models.CASCADE, verbose_name="code", null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.create_at}"
