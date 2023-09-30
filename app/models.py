from django.db import models


class Owner(models.Model):
    """Модель владельцев продуктов"""
    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name='имя')
    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель продукта"""
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE,
                              verbose_name='Владелец')
    title = models.CharField(max_length=255, unique=True,
                             verbose_name='Заголовок')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title

class Lesson(models.Model):
    """Модель для уроков"""
    product = models.ManyToManyField(Product,
                                      verbose_name='Продукт',)
    title = models.CharField(max_length=255, unique=True,
                             verbose_name='Название')
    link_to_video = models.URLField(unique=True,
                                    verbose_name='Ссылка')
    duration = models.PositiveIntegerField(verbose_name='Продолжительность')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.title
