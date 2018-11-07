# coding:utf-8
#

from django.urls import path
from ..openid import views

app_name = 'authentication'

urlpatterns = [
    # openid
    path('openid/login/', views.LoginView.as_view(), name='openid-login'),
    path('openid/login/complete/', views.LoginCompleteView.as_view(),
         name='openid-login-complete'),
    path('openid/logout/', views.LogoutView.as_view(), name='openid-logout')

    # other
]
