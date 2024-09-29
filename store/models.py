from django.db import models
from u_account.models import Profile


class Categories(models.Model):
    image = models.ImageField(upload_to="Media/Category Image")
    category_title = models.CharField(max_length=500,default="Consulting")

    def __str__(self):
        return self.category_title

class Area(models.Model):
    areas = models.CharField(max_length=100,default="UK")

    def __str__(self):
        return self.areas
    

class Job_details(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    job_description=models.TextField(max_length=200, blank=True, null=True)
    work_deadline=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)
    job_location=models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100,default="UK")
    rate_per_hour=models.PositiveIntegerField()
    job_image = models.ImageField(upload_to="Media/jobImage",default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeDkSNW9wtNePKrUAr1M8nbZvLO5AF8t0TMg&s")
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class FeaturesJobs(models.Model):
    jobs = models.ForeignKey(Job_details,on_delete=models.CASCADE)

    def __str__(self):
        return self.jobs.title

    




