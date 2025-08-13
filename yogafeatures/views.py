from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import YogaPlan, YogaCourse, UserSubscription
from django.contrib.auth.decorators import login_required

def plans_list(request):
    plans = YogaPlan.objects.all()
    return render(request, 'yogafeatures/plans.html', {'plans': plans})

def plan_detail(request, plan_id):
    plan = get_object_or_404(YogaPlan, id=plan_id)
    courses = plan.courses.all()
    return render(request, 'yogafeatures/plan_detail.html', {'plan': plan, 'courses': courses})

@login_required
def subscribe_plan(request, plan_id):
    plan = get_object_or_404(YogaPlan, id=plan_id)
    # Here we’ll integrate payment later — for now just mark as active
    UserSubscription.objects.create(user=request.user, plan=plan, active=True)
    return redirect('my_subscriptions')

@login_required
def my_subscriptions(request):
    subs = UserSubscription.objects.filter(user=request.user)
    return render(request, 'yogafeatures/my_subscriptions.html', {'subscriptions': subs})
