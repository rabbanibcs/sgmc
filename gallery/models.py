from django.db import models
from department.models import *
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(blank=True, max_length=200, default='Title here ...')
    image1 = models.ImageField(upload_to = 'pictures',null=True, blank=True)
    image2 = models.ImageField(upload_to = 'pictures',null=True, blank=True)
    image3 = models.ImageField(upload_to = 'pictures',null=True, blank=True)
    description = models.TextField(max_length=1000, default='Here should be desc...', blank=True)
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Carousel(models.Model):

    title = models.CharField(blank=True, max_length=200, default='Title here ...')
    image = models.ImageField(upload_to = 'carousel',null=True, blank=True)

    class Meta:
        verbose_name_plural = "Carousel"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Carousel_detail", kwargs={"pk": self.pk})

class NoticeBoard(models.Model):
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to = 'notice-board')
    created_on=models.DateTimeField(default=timezone.now)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
