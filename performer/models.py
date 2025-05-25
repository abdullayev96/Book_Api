from django.db import models
from baseapp.models import BaseModel



class Performer(BaseModel):
    full_name  = models.CharField(max_length=400, verbose_name="Ijrochining to'liq ismi")
    photo = models.ImageField(upload_to="images/", verbose_name="Ijrochi ni rasmi")
    bio  = models.TextField()


    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name  = "Ijrochi"
        verbose_name_plural = "Ijrochilar"

