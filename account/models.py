from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .manager import UserManager



class CustomUser(AbstractUser):
      username = models.CharField(max_length=300, unique=True)
      email =  models.EmailField(unique=True, blank=True)
      otp  = models.CharField(max_length=6, blank=True, null=True)
      is_staff = models.BooleanField(blank=False)



      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = []

      objects = UserManager()


      def save(self, *args, **kwargs):
          try:
             if kwargs['password']:
                  self.set_password(kwargs['password'])
          except Exception:
                       pass
          finally:
                super(CustomUser, self).save(*args, **kwargs)

      class Meta:
          db_table = 'account'
          verbose_name = _("User")
          verbose_name_plural = _("Users")

