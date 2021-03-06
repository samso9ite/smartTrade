from django.urls import path
from . import views

app_name = "adminPanel"

urlpatterns =[
   path("admin_dashboard", views.dashboard, name="admin_dashboard"),
   path("admin_create_card", views.CreateCardView.as_view(), name="admin_create_card"),
   path("view_transactions", views.AllTradeView.as_view(), name="admin_view_transactions"),
   path("view_feedback", views.FeedBackDetailView.as_view(), name="admin_view_feedback"),
   path("view_testimonials", views.TestimonialsView.as_view(), name="admin_view_testimonial"),
   path("view_cards", views.AllCardView.as_view(), name="admin_view_cards"),
   path("edit_card/<int:id>", views.UpdateCardDetails.as_view(), name="admin_edit_card"),
   # path("edit_trade/<int:id>", views.UpdateTrade.as_view(), name="admin_edit_trade"),
   path("set_card_rate/", views.addCardRate, name="set_card_rate"),
   path("all_card_rate", views.AllCardRate.as_view(), name="all_card_rate"),
   path("edit_rate/<int:id>", views.EditCardRate.as_view(), name="edit_rate"),
   path("delete_rate/<pk>", views.DeleteCardRate.as_view(), name="delete_rate"),
   path("approve_testimonial/<int:id>", views.approve_testimonial, name="approve_testimonial"),
   path('list_trade/<int:id>', views.viewTrades, name="view_trades"),
   path('approve_trade/<int:id>', views.setTradeStatus, name="approve_trade"),
   path('decline_trade/<int:id>', views.setTradeStatus, name="decline_trade"),
   path('view_trade_comment/<int:id>', views.view_trade_comment, name="view_trade_comment"),
   path("matured_points/", views.MaturedPoints.as_view(), name="matured_points"),
   path("all_users", views.AllUsers.as_view(), name="all_users"), 
   path("delete_card/<int:id>", views.deleteCard, name="delete_card")
]
    
