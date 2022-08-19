from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('locator/', views.locator, name='locator'),
    path('locator/<int:shop_id>/', views.locator_detail, name='detail'),
    path('locator/<int:shop_id>/add_review/', views.add_review, name='add_review'),
    path('locator/<int:pk>/update_review/', views.ReviewUpdate.as_view(), name='update_review'),
    path('locator/<int:pk>/delete_review/', views.ReviewDelete.as_view(), name='delete_review'),
]

