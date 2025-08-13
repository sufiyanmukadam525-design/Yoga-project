from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.plans_list, name='plans'),
    path('plans/<int:plan_id>/', views.plan_detail, name='plan_detail'),
    path('plans/<int:plan_id>/subscribe/', views.subscribe_plan, name='subscribe_plan'),
    path('my-subscriptions/', views.my_subscriptions, name='my_subscriptions'),
]
