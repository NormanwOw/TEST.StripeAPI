from django.db import models


class Item(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
        verbose_name='Название'
    )
    description = models.CharField(
        max_length=150,
        verbose_name='Название',
        blank=True
    )
    price = models.DecimalField(
        default=0.00,
        max_digits=7,
        decimal_places=2,
        verbose_name='Цена'
    )

    class Meta:
        db_table = 'item'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('id',)
