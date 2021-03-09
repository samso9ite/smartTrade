from django.shortcuts import render
from adminPanel.models import CardRateModel,TradeCardTypeModel
from tradersPanel.models import TestimonialModel 
from django.views.generic import ListView

# Create your views here.
def card_rate(request, id):
    rate = CardRateModel.objects.filter(is_active=True, card_type_id=id)
    return render(request, 'landing_page/card_rate.html', {'all_rate':rate}) 

class TestimonialsView(ListView):
    model = TestimonialModel
    template_name = 'landing_page/testimonials.html'
    context_object_name = "testimonials"  

    def get_queryset(self):
        testimonials = TestimonialModel.objects.filter(status=True)
        return testimonials


class AllCardView(ListView):
    model = TradeCardTypeModel
    context_object_name = "cards"
