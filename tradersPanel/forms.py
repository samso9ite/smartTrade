from django import forms
from tradersPanel.models import *

class tradersProfileForm(forms.ModelForm):
    
    class Meta:
        model= ProfileDetails
        fields = ('first_name', 'last_name', 'phone_number', 'profession', 'bank_accnt_number', 'bank_accnt_name', 'bank_name', 'referred_by')

    def clean_referred_by(self):
        referred_by= self.cleaned_data.get('referred_by')
        print(referred_by)
        if referred_by:
            if ProfileDetails.objects.filter(referral_code=referred_by).exists():
                pass
            else:
                raise forms.ValidationError("Referral Doesn't exist")
            return referred_by

class sendFeedBackForm(forms.ModelForm):

    class Meta:
        model = sendFeedBackModel
        fields = ('feedbackText', 'email_address',)


class testmonialForm(forms.ModelForm):

    class Meta:
        model = TestimonialModel
        fields = ('testimonialText',)    


class TradeForm(forms.ModelForm):

    class Meta:
            model = TradeModel
            fields = ('trade_card', 'price','quantity','trade')
          