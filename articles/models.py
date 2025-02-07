from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
class Categories(models.Model):
    name = models.CharField('Имя категории',max_length=200,unique=True)
    slug=models.SlugField('Slug',default='')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
class Products(models.Model):
    name = models.CharField('Имя категории',max_length=200,unique=True)
    img=models.URLField('Изображение',default='')
    cate=models.ForeignKey(Categories,verbose_name='Категория',on_delete=models.CASCADE)
    desc=RichTextField('Описание',default='none')
    slug=models.SlugField('Slug',default='')
    date=models.DateTimeField('Дата',default=timezone.now)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Продукт'
        verbose_name_plural='Продукты'