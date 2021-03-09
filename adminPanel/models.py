from django.db import models
from tradersPanel.models import MainTradeModel

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
   card_curr = models.CharField(max_length=100)
   card_amt = models.IntegerField()
   rate = models.CharField(max_length=255)
   is_active = models.BooleanField(default=True)

class TradeCommentModel(models.Model):
   trade = models.ForeignKey(MainTradeModel, on_delete=models.CASCADE)
   comment = models.CharField(max_length=255)
   
class CommentImgModel(models.Model):
   trade = models.ForeignKey(MainTradeModel, on_delete=models.CASCADE)
   comment_img = models.ImageField(upload_to='images/TradeComment',  null=True, blank=True)