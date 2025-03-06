import uuid
from django.db import models

# Create your models here.
from championship.models import championship
from userapp.models import User
from django.db import models


class order(models.Model):
    status = (
        ('pending','pending'),
        ('approved','approved'),
        ('rejected','rejected')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    championship = models.ForeignKey(championship, on_delete=models.CASCADE, related_name='registrations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=status, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order - {self.id} - {self.user.username} - {self.championship.name}"

