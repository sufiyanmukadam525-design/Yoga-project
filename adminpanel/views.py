from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
# Create your views here.


class AdminDashboardView(View):
    @method_decorator(login_required)
    def get(self, request):
        if hasattr(request.user, 'role') and request.user.role == 'admin':
            return render(request, 'adminpanel/admin_dashboard.html')
        elif request.user.is_superuser or request.user.is_staff:
            return render(request, 'adminpanel/admin_dashboard.html')
        else:
            messages.error(request, 'You do not have permission to view this page.')
            return redirect('home')

