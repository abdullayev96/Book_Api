from django.db import models
from account.models import CustomUser
# from baseapp.models import BaseModel



class Order(models.Model):
      NEW = "new"
      REJECTED = "rejected"
      COMPLETED = "completed"


      STATUS_CHOICES = (
          (NEW, 'new'),
          (REJECTED, 'rejected'),
          (COMPLETED, 'completed')
      )

      book_name = models.CharField(max_length=200, verbose_name="Kitob nomi")
      author_name  = models.CharField(max_length=400, verbose_name="Author to'liq ismi")
      comment  = models.TextField()
      answers = models.CharField(max_length=200)
      user  = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
      status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="new")


      def __str__(self):
          return self.book_name


      class Meta:
          verbose_name = "Zakas beruvchi"
          verbose_name_plural = "Zakas beruvchilar"
