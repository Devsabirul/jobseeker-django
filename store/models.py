from django.db import models
from u_account.models import Profile

# Create your models here.
class Job_details(models.Model):

    STATUS=(
        ('active', active),
        ('inactive', inactive)
    )

    JOB_STATUS=(
        ('inside', inside),
        ('outside', outside)
    )

    
    JOB_TYPE=(
        ('per_time', per_time),
        ('full_time', full_time)
    )

    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    jobname=models.CharField(max_length=50)
    job_description=models.TextField(max_length=200, blank=True, null=True)
    work_deadline=models.TimeField(blank=True, null=True)
    status=models.CharField(choices=STATUS, blank=true, null=true)
    job_status=models.CharField(choices=JOB_STATUS, blank=True, null=True)
    desirable_location=models.CharField(max_length=100, blank=True, null=True)
    rate_per_hour=models.PositiveIntegerField()
    job_type=models.CharField(choices=JOB_TYPE, blank=True, null=True)

    def __str__(self):
        return jobname






