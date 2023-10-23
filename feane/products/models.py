from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        unique=True,
        verbose_name='категория'
    )

    slug = models.SlugField(
        max_length=64,
        blank=False,
        null=False,
        unique=True,
        verbose_name='URL'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        unique=True,
        verbose_name='товар'
    )

    slug = models.SlugField(
        max_length=128,
        blank=False,
        null=False,
        unique=True,
        verbose_name='URL'
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='описание'
    )

    image = models.ImageField(
        upload_to='products_images',
        blank=False,
        null=False,
        verbose_name='картинка'
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=False,
        null=False,
        verbose_name='цена'
    )

    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
