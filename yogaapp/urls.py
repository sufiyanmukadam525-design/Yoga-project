from django.urls import path
from .views import Login, Register, HomeView, Logout

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('signup/',Register.as_view(), name='signup'),
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', Logout.as_view(), name='logout'),
]
