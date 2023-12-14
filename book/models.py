from django.db import models
from django.core.exceptions import ValidationError
from account.models import CustomUser
from baseapp.models import BaseModel
from author.models import Author
from performer.models import Performer
from category.models import Category



def validate_number(value):
    if value:
            if value>5:
                raise ValidationError("The number of team per pool is <=5. Please try again.")
    return value




class FileBook(models.Model):
      book = models.ForeignKey('Book', on_delete=models.CASCADE,  related_name='files')
      file  = models.FileField(upload_to='audio/', verbose_name="Faylni tanlang")

      class Meta:
          verbose_name = "Audio fayl"
          verbose_name_plural = "Audio fayllar"




class Book(BaseModel):
    name  = models.CharField(max_length=500, verbose_name="Kitobni nomi")
    description = models.TextField(verbose_name="Kitob haqida ")
    image = models.ImageField(upload_to='book/', blank=True, verbose_name="Kitobni rasmi")
    author = models.ForeignKey('author.Author', on_delete=models.CASCADE, verbose_name="Kitobning Muallifi", related_name="books")
    performer   = models.ForeignKey('performer.Performer', on_delete=models.CASCADE, verbose_name="Ijrochini Ism sharifi", related_name="per")
    category  = models.ForeignKey('category.Category', on_delete=models.CASCADE, verbose_name="Janrlar bo'limi", related_name="cat")



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural  = "Kitoblar"



class BookRead(BaseModel):
    book  = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Kitob nomi", related_name="book")
    score = models.IntegerField(validators=[validate_number])


    def __str__(self):
        return str(self.score)

    class Meta:
        verbose_name = "Baho"
        verbose_name_plural = "Baholar"
