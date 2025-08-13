from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class YogaPlan(models.Model):
    PLAN_TYPE_CHOICES = [
        ('Free', 'Free'),
        ('Subscription', 'Subscription'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    plan_type = models.CharField(max_length=20, choices=PLAN_TYPE_CHOICES, default='Free')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # for subscription
    image_url = models.URLField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class YogaCourse(models.Model):
    plan = models.ForeignKey(YogaPlan, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField(blank=True, null=True)  # optional for now
    order = models.PositiveIntegerField(default=0)  # sequence in plan

    def __str__(self):
        return f"{self.plan.title} - {self.title}"


class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(YogaPlan, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan.title}"
