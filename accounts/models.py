from django.db import models
from django.contrib.auth.models import User


# Create your models here.
CATEGORY_CHOICES = [
    ('Electronics', 'Electronics'),
    ('Men Clothing', ' Men Clothing'),
    ('women Clothing', ' Women Clothing'),
    ('Books', 'Books'),
    ('Home Appliances', 'Home Appliances'),
    ('Groceries','Groceries'),
]

class Product(models.Model):
    CATEGORY_CHOICES = [
    ('Electronics', 'Electronics'),
    ('Men Clothing', ' Men Clothing'),
    ('women Clothing', ' Women Clothing'),
    ('Books', 'Books'),
    ('Home Appliances', 'Home Appliances'),
    ('Groceries','Groceries'),
]
    image = models.ImageField(upload_to='images/')  # Correct syntax
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Electronics')

    def __str__(self):
        return self.name



class TeamMember(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

    def get_total_price(self):
        return self.product.price * self.quantity




class Categories(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Optional image
    name = models.CharField(max_length=100)  # Changed name1 to name for clarity
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return self.name  # Returns the category name when displayed in the admin