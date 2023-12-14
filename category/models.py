from django.db import models
from baseapp.models import BaseModel




class Category(BaseModel):
    name=models.CharField(max_length=300, verbose_name="Kategoriya nomi")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
