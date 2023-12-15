from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from . import models


@receiver(pre_save, sender=models.Cart)
def my_cart_pre_handler(sender, instance, **kwargs):
    if instance.pk:
        instance.total_amount = sum(cart_item.subtotal for cart_item in instance.cartitem_set.all())


@receiver(post_save, sender=models.CartItem)
def my_cartitem_post_handler(sender, instance, created, **kwargs):
    instance.cart.save()


@receiver(post_delete, sender=models.CartItem)
def my_cartitem_delete_handler(sender, instance, **kwargs):
    instance.cart.save()