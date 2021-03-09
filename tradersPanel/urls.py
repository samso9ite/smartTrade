from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = "tradersPanel"

urlpatterns = [
    path('traders_dashboard/', views.dashboard, name="dashboard"),
    path('profile_settings/', views.ProfileCreationView.as_view(), name="profile_settings"),
    path('update_profile/<int:id>', views.UpdateProfileView.as_view(), name="update_profile"),
    path('feedback/', views.sendFeedBackView.as_view(), name="send_feedback"),
    path('testimonial/', views.TestimonialCreateView.as_view(), name="send_testimonial"),
    path('view_feedbacks/', views.feedBackDetailView.as_view(), name="view_feedbacks"),
    path('trade_create/', views.TradeCreateView.as_view(), name="create_trade"),
    path('trade_create_api/', views.create_trade, name="create_trade_api"),
    path('view_trades/', views.AllTradeView.as_view(), name="view_trades"),
    path('select_card/', TemplateView.as_view(template_name='tradersPanel/select_card_type.html')),
    path('all_card', views.AllCardView.as_view(), name="all_card"),
    path('trade_calculator/<int:id>', views.trade_calculator, name="trade_calculator"),
    path('view_trade_comment/<int:id>', views.view_trade_comment, name="view_trade_comment")
]
