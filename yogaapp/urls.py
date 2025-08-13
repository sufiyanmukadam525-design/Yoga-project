from django.urls import path
from .views import HomeView, Register, Login, Logout, Base

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', Register.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('base/', Base.as_view(), name='base'),
]
