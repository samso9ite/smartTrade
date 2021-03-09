from django.db import models

# Create your models here.

class TradeCardTypeModel(models.Model):
   name = models.CharField(max_length=255)
   is_active = models.BooleanField(default=True)
   
   def __str__(self):
      return self.name

   class Meta:
      db_table = 'trade_card_type'
      managed = True
      verbose_name = 'TradeCardTypeModel'
      verbose_name_plural = 'TradeCardTypeModels'

class CardRateModel(models.Model):
   card_type = models.ForeignKey(TradeCardTypeModel, on_delete=models.CASCADE)
   card_curr = models.CharField(max_length=10)
   card_amt = models.IntegerField()
   rate = models.CharField(max_length=30)
   is_active = models.BooleanField(default=True)
 
