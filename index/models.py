from django.db import models

# Create your models here.
# Создаём таблицу категорий товаров
class Category(models.Model):
    category_name = models.CharField(max_length=64)

    def __str__(self):
        return str(self.category_name)

# Создаём таблицу для товаров
class Product(models.Model):
    product_name = models.CharField(max_length=256)
    product_desc = models.TextField()
    product_price = models.FloatField()
    product_count = models.IntegerField()
    product_photo = models.ImageField(upload_to='media')
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product_name)

#Таблица корзины
class Cart(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_pr_count = models.IntegerField()