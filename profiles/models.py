from django.db import models
from django.db import models
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from core.models import TimeStampModel

class CustomManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

def image_placer(instance, file_name):
    ext = file_name.split('.')[-1]
    return 'profile_images/' + instance.username + '.' + ext

class Profile(AbstractBaseUser, PermissionsMixin, TimeStampModel):

    objects = CustomManager()

    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    image = models.ImageField(upload_to=image_placer, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    follows = models.ManyToManyField("self", related_name='followed_by', null=True, blank=True)
    favourite = models.ManyToManyField("articles.Article", related_name='favourited_by', null=True, blank=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

    def save(self, **kwargs):
        if self.slug == '' or self.slug == None:
            self.slug = slugify(self.username)
        super(Profile, self).save(**kwargs)

    def get_absolute_url(self):
        return reverse_lazy("profile:profile", kwargs={"slug": self.slug})
    