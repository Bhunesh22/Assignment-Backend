from django.db import models
from users.models import User
import uuid
# Create your models here.


class Orders(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    tradingsymbol = models.CharField(max_length=100, blank=True, null=True)
    exchange = models.CharField(max_length=100, blank=True, null=True)
    isin = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    authorised_date = models.CharField(max_length=100, blank=True, null=True)
    average_price = models.FloatField(blank=True, null=True)
    last_price = models.FloatField(blank=True, null=True)
    close_price = models.FloatField(blank=True, null=True)
    pnl = models.FloatField(blank=True, null=True)
    day_change = models.FloatField(blank=True, null=True)
    day_change_percentage = models.FloatField(blank=True, null=True)
    order_id = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=False, auto_now=True)
    modified_at = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return str(self.user)
