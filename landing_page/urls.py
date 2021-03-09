from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "landing_page"
urlpatterns =[
    path("", views.TestimonialsView.as_view(template_name='landing_page/index.html'),  name="home_page"),
    path("all_cards", views.AllCardView.as_view(template_name='landing_page/all_cards.html'), name="all_cards"),
    path("card_rate/<int:id>", views.card_rate, name="card_rate"),
    path("all_testimonials", views.TestimonialsView.as_view(),  name="all_testimonials")
]