from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Core Pages
    path('', views.home, name='home'),  
    path('signup/', views.signup_view, name='signup'),  
    path('login/', views.login_view, name='login'),  
    path('setup/', views.setup_view, name='setup'),  
    path('setup/dashboard/', views.dashboard, name='dashboard'),  

    # Password Reset
    path('forgot-password/', views.forgot_password, name='forgot_password'), 
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),

    # Health & Analytics Features
    path('save_health_data/', views.save_health_data, name='save_health_data'),
    path('healthMetrics/', views.healthMetrics, name='healthMetrics'),
    path('chatAI/', views.chatAI, name='chatAI'),
    path('visualInsights/', views.visualInsights, name='visualInsights'),
    path('setGoals/', views.setGoals, name='setGoals'),
    path('trackProgress/', views.trackProgress, name='trackProgress'),
    path('dietPlan/', views.dietPlan, name='dietPlan'),

    # External Integrations
    path('news/', views.get_health_news, name='get_health_news'),
    path('oauth/callback/', views.oauth_callback, name='oauth_callback'),
    path('fetch-google-fit/', views.fetch_google_fit_data, name='fetch_google_fit_data'),
    path('save-google-fit-data/', views.save_google_fit_data, name='save_google_fit_data'),
]
