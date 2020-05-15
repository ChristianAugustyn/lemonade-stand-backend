from django.db import models

# Create your models here.
class StaffMember(models.Model):

    POSITIONS = [
        ('junior', 'Junior'),
        ('senior', 'Senior'),
        ('manager', 'Manager')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(
        choices=POSITIONS, 
        max_length=50
    )
    commission = models.DecimalField(max_digits=3, decimal_places=0)

    class Meta:
        unique_together = (('first_name', 'last_name'),)