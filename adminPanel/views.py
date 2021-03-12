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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def dashboard(request):
    total_users = User.objects.all().count()
    total_transactions = MainTradeModel.objects.all().count()
    pending_transactions = MainTradeModel.objects.filter(status='1').count()
    all_trades =  MainTradeModel.objects.all().order_by('-id')[:20]
    matured_points = ProfileDetails.objects.filter(referral_point__gte=10).count()

    page = request.GET.get('page', 1)
    paginator = Paginator(all_trades, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request,'adminPanel/admin_dashboard.html',
            {'all_trades':all_trades,'total_users':total_users,'total_transactions':total_transactions,'pending_transactions':pending_transactions, 'matured_points':matured_points})


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
    ordering =['-id']

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
    model = MainTradeModel
    context_object_name = "trades"
    template_name = "adminPanel/transactions.html"
    ordering = ['-id']
    paginate_by = 10

# @method_decorator(login_required, name='dispatch')
# class UpdateTrade(UpdateView):
#     model = MainTradeModel
#     form_class = UpdateTradeForm
#     template_name = 'adminPanel/trade_edit.html'
#     success_url = reverse_lazy('adminPanel:admin_view_transactions')
    

#     def get_object(self, *args, **kwargs):
#         trade = get_object_or_404(TradeModel, pk=self.kwargs['id'])
#         return trade

#     def form_valid(self, form):
#         user = self.request.user    
#         form.instance.user = user
#         return super().form_valid(form)
    
@login_required
def viewTrades(request, id):
    details=""
    trades = TradeModel.objects.filter(trade_id=id)
    images = ImageModel.objects.filter(trade_line=id)
    extra_details = MainTradeModel.objects.get(id=id)
    if extra_details.default_bank_details is True:
        details = ProfileDetails.objects.get(User_id=extra_details.user_id)
    return render(request, 'adminPanel/trade_edit.html', {'trades':trades, 'images':images, 'extra_details':extra_details, 'details':details})  
 
@login_required
def setTradeStatus(request, id):
    if 'approve_trade' in request.path:
        trade = MainTradeModel.objects.filter(id=id).update(status=2)
        messages.success(request, "Trade Approved", extra_tags='alert')
    elif 'decline_trade' in request.path:
        object_id = MainTradeModel.objects.get(id=id)
        form = TradeCommentForm(request.POST)
        imgForm = CommentImgForm(request.POST, request.FILES)
        if request.method == 'POST' :
            if form.is_valid() and imgForm.is_valid():
                form.save(commit=False) and imgForm.save(commit=False)
                form.instance.trade = object_id
                form.save()
                all_images = request.FILES.getlist('comment_img')
                for img in all_images:
                    CommentImgModel.objects.create(comment_img=img, trade=object_id)
            else:
                print(form.errors)
        messages.success(request, "Trade Declined", extra_tags='alert')
        object_id.status=3
        object_id.save()

    return HttpResponseRedirect(reverse_lazy('adminPanel:admin_view_transactions'))

@method_decorator(login_required, name="dispatch")
class FeedBackDetailView(ListView):
    model = sendFeedBackModel
    template_name = 'adminPanel/feedback.html'
    context_object_name = "feedback_data"
    ordering = ['-id']

@method_decorator(login_required, name="dispatch")
class TestimonialsView(ListView):
    model = TestimonialModel
    template_name = 'adminPanel/testimonials.html'
    context_object_name = "testimonials"   
    ordering = ['-id']

@login_required
def approve_testimonial(request, id):
    testimonial = TestimonialModel.objects.get(id=id)
    testimonial.status = True
    testimonial.save()
    return HttpResponseRedirect(reverse_lazy('adminPanel:admin_view_testimonial'))

@login_required
def addCardRate(request):
    form = NewRateForm(request.POST or None)
    card_type = TradeCardTypeModel.objects.all()
    context = {'cards': card_type, 'form':form}
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
    ordering = ['-id']
    paginate_by=10

@method_decorator(login_required, name="dispatch")
class EditCardRate(UpdateView):
    model = CardRateModel
    template_name = 'adminPanel/new_card_rate.html'
    form_class = UpdateRateForm
    success_url = reverse_lazy('adminPanel:all_card_rate')

    def get_object(self, *args, **kwargs):
        rate = get_object_or_404(CardRateModel, pk=self.kwargs['id'])
        return rate

@method_decorator(login_required, name="dispatch")
class DeleteCardRate(DeleteView):
    model = CardRateModel
    success_url = reverse_lazy('adminPanel:all_card_rate')

@login_required
def view_trade_comment(request, id):
    details=""
    trades = TradeModel.objects.filter(trade_id=id)
    try:      
        images = CommentImgModel.objects.filter(trade_id=id)
    except CommentImgForm.DoesNotExist:
        images = None
    extra_details = MainTradeModel.objects.get(id=id)
    trade_comment = TradeCommentModel.objects.filter(trade_id=id)
    if extra_details.default_bank_details is True:
        details = ProfileDetails.objects.get(User_id=extra_details.user_id)
    return render(request, 'adminPanel/view_trade_comment.html', {'trades':trades, 'trade_comment':trade_comment, 'images':images, 'extra_details':extra_details, 'details':details})  
 
@method_decorator(login_required, name="dispatch")
class MaturedPoints(ListView):
    model = ProfileDetails
    template_name = 'adminPanel/matured_points.html'
    context_object_name = 'matured_points'
    paginate_by = 10

    def get_queryset(self):
        matured_points = ProfileDetails.objects.filter(referral_point__gte=10)
        print(matured_points)
        return matured_points
