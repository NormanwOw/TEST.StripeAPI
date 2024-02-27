from django.db import models


class Order(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        db_table = 'order'
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ('-created',)

    def __str__(self):
        return f'№{self.pk}'

    def get_total_usd_cost(self) -> int:
        """Sum costs with different currency's"""

        MOCK_EUR_USD_RATE = 1.09

        prices = []
        for item in self.items.all():
            if item.currency == 'eur':
                price = float(item.price) * MOCK_EUR_USD_RATE
            else:
                price = float(item.price)
            prices.append(price)

        return int(sum(prices))


class Item(models.Model):
    CUR = {
        'usd': 'usd',
        'eur': 'eur'
    }
    name = models.CharField(
        max_length=32,
        unique=True,
        verbose_name='Название'
    )
    description = models.CharField(
        max_length=150,
        verbose_name='Описание',
        blank=True
    )
    price = models.DecimalField(
        default=0.00,
        max_digits=7,
        decimal_places=2,
        verbose_name='Цена'
    )
    currency = models.CharField(
        max_length=3,
        choices=CUR,
        verbose_name='Валюта',
        default='usd'
    )
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.PROTECT,
        verbose_name='Заказ'
    )

    class Meta:
        db_table = 'item'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('id',)

    def __str__(self):
        return self.name

