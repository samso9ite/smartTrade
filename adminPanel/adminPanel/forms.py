from django import forms
from .models import *
from tradersPanel.models import TradeModel

class CardTypeForm(forms.ModelForm):

    class Meta:
            model = TradeCardTypeModel
            fields = ('name','is_active')

class UpdateTradeForm(forms.ModelForm):

    class Meta:
            model = TradeModel
            fields = ('trade_card','quantity','status')



class NewRateForm(forms.ModelForm):
    
    class Meta:
          model = CardRateModel
          fields = '__all__'