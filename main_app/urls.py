from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('locator/', views.locator, name='locator'),
    path('locator/<int:shop_id>/', views.locator_detail, name='detail'),
]
