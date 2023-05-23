from django.contrib.auth.models import User, AbstractUser
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class Goods(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    url = models.SlugField()
    charecterist = RichTextUploadingField()
    delivery = models.BooleanField(default=False)
    amount = models.IntegerField()
    image = models.ImageField(upload_to='static/img')
    date = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)
    assess = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'from {self.user} in {self.good}'


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    text = models.CharField(max_length=10000)
    date = models.DateTimeField(default=timezone.now())


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    active = models.BooleanField(default=False)
<<<<<<< HEAD
    items = models.ManyToManyField(Goods, through='BasketItems')

    def get_cart_total(self):
        return sum([item.item.price for item in self.item.all()])


class BasketItems(models.Model):
    basket = models.OneToOneField(Basket, on_delete=models.CASCADE, default=None)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=0)
=======


class BasketItems(models.Model):
    item = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='items', default=None)
    quantity = models.IntegerField(default=0)


class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, default=None)
    order_items = models.ManyToManyField(BasketItems,  blank=True, default=list)
    is_ordered = models.BooleanField(default=False)


    def get_cart_total(self):
        return sum([item.item.price for item in self.order_items.all()])

>>>>>>> origin/main
