from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from registration import views
# from django.conf.urls import url,


app_name = "registration"
urlpatterns =[
path('sign_up', views.signUpView, name="sign_up"),
path('sign_in', views.loginView, name="sign_in"),
path('sign_out', views.signoutView , name="sign_out"),
path('password_reset/', auth_views.PasswordResetView.as_view(template_name="reset_pwd/password_reset_form.html", email_template_name="reset_pwd/password_reset_email.html", subject_template_name="reset_pwd/password_reset_subject.txt", success_url=reverse_lazy('registration:password_reset_done')), name="password_reset"),
path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="reset_pwd/password_reset_done.html"), name="password_reset_done"),
path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset_pwd/password_reset_confirm.html", success_url=reverse_lazy('registration:password_reset_complete')), name="password_reset_confirm"),
path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_pwd/password_reset_complete.html"), name="password_reset_complete"),
path('thank_you/', TemplateView.as_view(template_name="registration/thank_you.html"), name="thank_you"),
# url(r'^oauth/', include('social_django.urls', namespace='social')), 
]