from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255, verbose_name="Full Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"
