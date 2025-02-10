from django.db import models
class MainTexts(models.Model):
    float1=models.CharField('Текст 1',max_length=200,default='none')
    float2=models.CharField('Текст 2',max_length=200,default='none')
    float3=models.CharField('Текст 3',max_length=200,default='none')
    about=models.TextField('О нас',default='none')
    addressTxt=models.CharField('Адрес',max_length=200,default='none')
    addressUrl=models.URLField('Ссылка адреса',default='none')
    phone=models.CharField('Телефон',max_length=200,default='none')
    whatsapp=models.CharField('Whatsapp',max_length=200,default='none')
    telegram=models.CharField('Telegram',max_length=200,default='none')
    def __str__(self):
        return f'Все тексты из главной страницы'
    class Meta:
        verbose_name = 'Все тексты из главной страницы'
        verbose_name_plural = 'Все тексты из главной страницы'
class HeaderBackgroud(models.Model):
    img = models.URLField(default='none')
    def __str__(self):
        return f'Изображение {self.id}'
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
class Partners(models.Model):
    name = models.CharField('Название',max_length=200)
    img = models.URLField(default='none')
    def __str__(self):
        return f'Партнер'
    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
class AboutInFooter(models.Model):
    txt=models.TextField('Текст',default='none')
    def __str__(self):
        return f'О нас на футере'
    class Meta:
        verbose_name = 'О нас на футере'
        verbose_name_plural = 'О нас на футере'