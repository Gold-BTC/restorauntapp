from django.db import models

class Category (models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Назва категорii')
    description = models.TextField(null=True, blank=True, verbose_name='Опис категорii')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'категорiя'
        verbose_name_plural = 'категорii'

class Dish (models.Model):
    title = models.CharField(max_length=100,verbose_name='Назва страви')
    description = models.TextField(null=True, blank=True,verbose_name='Опис страви')
    price = models.FloatField(verbose_name='Цiна страви')
    photo = models.ImageField(upload_to='dishes/', null=True, blank=True, verbose_name='Фото страви')
    availability = models.BooleanField(default=True, verbose_name='Наявнiсть')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes', verbose_name='Категорiя страви')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('cash', 'Готівка'),
        ('card', 'Картка при отриманні'),
        ('online', 'Онлайн оплата'),
    ]
    customer_name = models.CharField(max_length=100, verbose_name='Ім\'я клієнта')
    customer_phone = models.CharField(max_length=20, verbose_name='Телефон клієнта')
    customer_address = models.CharField(max_length=255, verbose_name='Адреса клієнта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення замовлення')
    total_price = models.FloatField(verbose_name='Загальна ціна замовлення')
    payment_metod = models.CharField(max_length=50, choices=PAYMENT_CHOICES, verbose_name='Спосiб оплати')

    def __str__(self):
        return f'Замовлення {self.id} - {self.customer_name}'
    
    class Meta:
        verbose_name = 'Завмовлення'
        verbose_name_plural = 'Замовлення'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='Замовлення')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name='Страва')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Кiлькiсть')

    def __str__(self):
        return f'{self.quantity} x {self.dish.title} for Order {self.order.id}'
    
    class Meta:
        verbose_name = 'Позицiя в замовленнi'
        verbose_name_plural = 'Позицii замовлення'