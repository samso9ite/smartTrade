from django.shortcuts import render
from tradersPanel.models import *
from adminPanel.models import *
from django.views.generic import CreateView, UpdateView, DetailView, ListView,TemplateView
from django.contrib.auth.decorators import login_required
from tradersPanel.forms import *
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@login_required
def dashboard(request):
    total_transactions = MainTradeModel.objects.filter(user=request.user.id).count()
    pending_transactions = MainTradeModel.objects.filter(status='1',user=request.user.id).count()

    all_trades =  MainTradeModel.objects.filter(user=request.user.id).order_by('-id')[:20]
    try:
        profile = ProfileDetails.objects.get(User_id=request.user.id)
    except ProfileDetails.DoesNotExist:
        profile=None

    return render(request,'tradersPanel/trader_dashboard.html',
            {'all_trades':all_trades,'total_transactions':total_transactions,'pending_transactions':pending_transactions, 'profile':profile})

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ProfileCreationView(SuccessMessageMixin, CreateView):
    model = ProfileDetails
    form_class = tradersProfileForm
    template_name = 'tradersPanel/setting.html'
    success_url = reverse_lazy('tradersPanel:dashboard')
    success_message = "It was created successfully"
    
    def form_valid(self, form):
        user = self.request.user
        form.instance.User = user
        form.instance.updated = True
        referral_code =  ProfileDetails.objects.filter(referral_code=form.instance.referred_by)
        referral_code.update(referral_point=F('referral_point')+5)
        
        return super().form_valid(form)
    
    def get_object(self):
        referral_code =  get_object_or_404(ProfileDetails, referral_code=self.req)
        print(referral_code)

@method_decorator(login_required, name="dispatch")
class UpdateProfileView(SuccessMessageMixin, UpdateView):
    model = ProfileDetails
    form_class = tradersProfileForm
    template_name = 'tradersPanel/update_profile.html'
    context_object_name = 'update_data'
    success_url = reverse_lazy('tradersPanel:dashboard')
    success_message = "Profile Updated Successfully"

    def get_object(self):
        update_data= get_object_or_404(self.model, User_id=self.request.user.id)
        return update_data

@method_decorator(login_required, name="dispatch")
class sendFeedBackView(SuccessMessageMixin, CreateView):
    model = sendFeedBackModel
    form_class = sendFeedBackForm
    template_name = 'tradersPanel/feedback.html'
    success_url = reverse_lazy('tradersPanel:view_feedbacks')
    success_message = "Testimonial Submitted"

    def form_valid(self, form):
        user = self.request.user    
        form.instance.User = user
        return super().form_valid(form)

@method_decorator(login_required, name="dispatch")
class TestimonialCreateView(SuccessMessageMixin, CreateView):
    model = TestimonialModel
    form_class = testmonialForm
    template_name = 'tradersPanel/testimonials.html'
    success_url = reverse_lazy('tradersPanel:dashboard')
    success_message = "Testimonial Submitted"

    def form_valid(self, form):
        user = self.request.user    
        form.instance.user = user
        return super().form_valid(form)

@method_decorator(login_required, name="dispatch")
class feedBackDetailView(ListView):
    model = sendFeedBackModel
    template_name = 'tradersPanel/feedback_details.html'
    context_object_name = "feedback_data"

@method_decorator(login_required, name="dispatch")
class TradeCreateView(SuccessMessageMixin, TemplateView):
    template_name = 'tradersPanel/calculator.html'

    def get_context_data(self, **kwargs):
        context = super(TradeCreateView, self).get_context_data(**kwargs)
        context['cards']= TradeCardTypeModel.objects.filter(is_active=True)
        return context

@method_decorator(login_required, name='dispatch')
class AllTradeView(ListView):
    model = MainTradeModel
    context_object_name = "trades"
    template_name = "tradersPanel/trade_history.html"
    ordering = '-id'
    paginate_by=20

    def get_queryset(self):
        trades = MainTradeModel.objects.filter(user=self.request.user.id)
        return trades

 
@csrf_exempt
@login_required
def create_trade(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        bank_name = post_data['bank_name']
        bank_accnt_num = post_data['bank_accnt_num']
        bank_accnt_name = post_data['bank_accnt_name']
        default_details = post_data['default_accnt']
        total_amount = post_data['total_amount']
        if default_details == 'true':
            default_bank_details = True
        else:
            default_bank_details= False
        reference = post_data['reference']
        try:
            main_trade = MainTradeModel.objects.create(user=request.user,reference=reference,bank_accnt_name=bank_accnt_name,
            bank_accnt_num=bank_accnt_num,bank_name=bank_name, default_bank_details=default_bank_details, total_amount=total_amount)
        except IntegrityError:
            main_trade = MainTradeModel.objects.get(reference=reference)  

        post_data.update({'user':request.user.id,'trade':main_trade.id})
        form = TradeForm(post_data)
        if form.is_valid():
            res = form.save()
            all_images = request.FILES.getlist('image[]')
 
            for image in all_images:
                ImageModel.objects.create(image=image,trade_line=main_trade.id)
            messages.success(request,"Trade Created")
            subject = 'A new trade has been created'
            html_message = render_to_string('tradersPanel/mail_template.html', {'context': 'values'})
            plain_message = strip_tags(html_message)
            from_email = 'From <info@smartrade.ng>'
            to = 'samso9ite@gmail.com'

            mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
            return JsonResponse({'status':True,'message':'Trade Created'})
        else:
            return JsonResponse({'status': False, 'message': form.errors})

@method_decorator(login_required, name='dispatch')
class AllCardView(ListView):
    model = TradeCardTypeModel
    context_object_name = "cards"
    template_name = "tradersPanel/cards.html"
    ordering = '-id'

@login_required
def trade_calculator(request, id):
    bank_details =''
    cards = CardRateModel.objects.filter(is_active=True, card_type_id=id)
    try:
        bank_details = ProfileDetails.objects.get(User_id=request.user.id)
    except ProfileDetails.DoesNotExist:
        pass
    return render(request, 'tradersPanel/calculator.html', {'cards':cards, 'bank_details':bank_details}) 

@login_required
def view_trade_comment(request, id):
    details=""
    trades = TradeModel.objects.filter(trade_id=id)
    images = CommentImgModel.objects.filter(trade_id=id)
    extra_details = MainTradeModel.objects.get(id=id)
    trade_comment = TradeCommentModel.objects.filter(trade_id=id)
    if extra_details.default_bank_details is True:
        details = ProfileDetails.objects.get(User_id=extra_details.user_id)
    return render(request, 'tradersPanel/view_trade.html', {'trades':trades, 'trade_comment':trade_comment, 'images':images, 'extra_details':extra_details, 'details':details})  
 