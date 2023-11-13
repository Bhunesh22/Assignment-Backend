from django.db import models
# Create your models here.


class HistoriclaData(models.Model):
    index = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField( blank=True, null=True)
    price = models.FloatField( blank=True, null=True)
    instrument_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateField(auto_now_add=False, auto_now=True)
    modified_at = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        db_table = 'historical price data'

    def __str__(self):
        return str(self.date)
