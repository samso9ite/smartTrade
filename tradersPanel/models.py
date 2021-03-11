from django.db import models
from django.contrib.auth.models import User
# from adminPanel.models import CardRateModel
import uuid
# Create your models here.


class MainTradeModel(models.Model):
    STATUS = [
        ('1','Pending'),
        ('2','Success'),
        ('3','Failed')
    ]

    reference = models.CharField(max_length=255,default=uuid.uuid4,unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS,max_length=10,default='1')
    created_at = models.DateTimeField(auto_now=True)
    default_bank_details = models.BooleanField(default=False)
    bank_accnt_name = models.CharField(max_length=225, null=True, blank=True)
    bank_accnt_num = models.CharField(max_length=100, null=True, blank=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    total_amount = models.CharField(max_length=100, null=True, blank=True)


    def trade_lines(self):
        return self.trade_lines

class TradeModel(models.Model):
    trade = models.ForeignKey(MainTradeModel,on_delete=models.CASCADE,null=True,related_name="trade_lines")
    trade_card = models.ForeignKey('adminPanel.CardRateModel',on_delete=models.SET_NULL,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=20)
    image = models.ImageField(upload_to="trade_card",null=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    
    def total_amount(self):
        return self.quantity * self.price

    class Meta:
        db_table = 'trades'
        managed = True
        verbose_name = 'TradeModel'
        verbose_name_plural = 'TradeModels'

class ImageModel(models.Model):
    trade_line = models.CharField(max_length=200)
    image = models.ImageField(upload_to="trade_card", null=True)

    class Meta:
        db_table = 'images'
        managed = True
        verbose_name = 'ImageModel'
        verbose_name_plural = 'ImageModels'
        
class ProfileDetails(models.Model):
    User =  models.OneToOneField(User, on_delete=models.CASCADE)
    updated = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    bank_accnt_number = models.CharField(max_length=50)
    bank_accnt_name = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=50) 
    referred_by = models.CharField(max_length=8, blank=True, null=True)
    referral_code = models.CharField(max_length=8, default=uuid.uuid4,unique=True)
    profile_img = models.ImageField(upload_to='images/profImg',  null=True, blank=True)
    referral_point = models.IntegerField(blank=True, default=0)

class sendFeedBackModel(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    feedbackText = models.CharField(max_length=254)
    email_address = models.EmailField(max_length=254, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

class TestimonialModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    testimonialText = models.CharField(max_length=254)
    status = models.BooleanField(default=False)
