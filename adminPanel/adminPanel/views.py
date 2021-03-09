from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView, ListView,TemplateView, View, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import messages
from adminPanel.models import *
from adminPanel.forms import *
from tradersPanel.models import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.


def dashboard(request):
   total_users = User.objects.all().count()
   total_transactions = TradeModel.objects.all().count()
   pending_transactions = TradeModel.objects.filter(status='1').count()
   all_trades =  TradeModel.objects.all()
   return render(request,'adminPanel/admin_dashboard.html',
            {'all_trades':all_trades,'total_users':total_users,'total_transactions':total_transactions,'pending_transactions':pending_transactions})


@method_decorator(login_required, name="dispatch")
class CreateCardView(SuccessMessageMixin, CreateView):
    model = TradeCardTypeModel
    form_class = CardTypeForm
    template_name = 'adminPanel/new_card.html'
    success_url = reverse_lazy('adminPanel:admin_view_cards')
    success_message = "Card Created"



@method_decorator(login_required, name='dispatch')
class AllCardView(ListView):
    model = TradeCardTypeModel
    context_object_name = "cards"
    template_name = "adminPanel/cards.html"


@method_decorator(login_required, name='dispatch')
class UpdateCardDetails(UpdateView):
    model = TradeCardTypeModel
    fields = '__all__'
    template_name = 'adminPanel/card_edit.html'
    success_url = reverse_lazy('adminPanel:admin_view_cards')
    

    def get_object(self, *args, **kwargs):
        card = get_object_or_404(TradeCardTypeModel, pk=self.kwargs['id'])
        return card
 


@method_decorator(login_required, name='dispatch')
class AllTradeView(ListView):
    model = TradeModel
    context_object_name = "trades"
    template_name = "adminPanel/transactions.html"
 

@method_decorator(login_required, name='dispatch')
class UpdateTrade(UpdateView):
    model = TradeModel
    form_class = UpdateTradeForm
    template_name = 'adminPanel/trade_edit.html'
    success_url = reverse_lazy('adminPanel:admin_view_transactions')
    

    def get_object(self, *args, **kwargs):
        trade = get_object_or_404(TradeModel, pk=self.kwargs['id'])
        return trade

    def form_valid(self, form):
        user = self.request.user    
        form.instance.user = user
        return super().form_valid(form)
 

@method_decorator(login_required, name="dispatch")
class FeedBackDetailView(ListView):
    model = sendFeedBackModel
    template_name = 'adminPanel/feedback.html'
    context_object_name = "feedback_data"
    

@method_decorator(login_required, name="dispatch")
class TestimonialsView(ListView):
    model = TestimonialModel
    template_name = 'adminPanel/testimonials.html'
    context_object_name = "testimonials"   

@login_required
def approve_testimonial(request, id):
    testimonial = TestimonialModel.objects.get(id=id)
    print(testimonial)
    testimonial.status = True
    testimonial.save()
    return HttpResponseRedirect(reverse_lazy('adminPanel:admin_view_testimonial'))

@login_required
def addCardRate(request):
    form = NewRateForm(request.POST or None)
    card_type = TradeCardTypeModel.objects.all()
    context = {'cards': card_type, 'form':form}
    print(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "New Rate Created", extra_tags='alert')
    else:
        form = NewRateForm()
    return render(request, 'adminPanel/new_card_rate.html', context)

@method_decorator(login_required, name="dispatch")
class AllCardRate(ListView):
    model = CardRateModel
    context_object_name = 'card_rate'
    template_name = 'adminPanel/card_rate.html'

@method_decorator(login_required, name="dispatch")
class EditCardRate(UpdateView):
    model = CardRateModel
    template_name = 'adminPanel/new_card_rate.html'
    form_class = NewRateForm
    success_url = reverse_lazy('adminPanel:all_card_rate')

    def get_object(self, *args, **kwargs):
        rate = get_object_or_404(CardRateModel, pk=self.kwargs['id'])
        return rate

@method_decorator(login_required, name="dispatch")
class DeleteCardRate(DeleteView):
    model = CardRateModel
    success_url = reverse_lazy('adminPanel:all_card_rate')
