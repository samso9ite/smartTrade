from django import forms
from .models import *
from tradersPanel.models import TradeModel

class CardTypeForm(forms.ModelForm):

    class Meta:
            model = TradeCardTypeModel
            fields = ('name','is_active')

# class UpdateTradeForm(forms.ModelForm):

#     class Meta:
#             model = TradeModel
#             fields = ('trade_card','quantity')



class NewRateForm(forms.ModelForm):
    
    class Meta:
          model = CardRateModel
          fields = '__all__'

class UpdateRateForm(forms.ModelForm):
    
    class Meta:
          model = CardRateModel
          exclude = ('card_type',)

class TradeCommentForm(forms.ModelForm):

    class Meta:
        model = TradeCommentModel
        exclude = ('trade',)

class CommentImgForm(forms.ModelForm):
    class Meta:
        model = CommentImgModel
        exclude = ('trade',)