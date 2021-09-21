from django.db import models

# Create your models here.

STATUS_CHOICES = [
    ('A', 'Accept'),
    ('P', 'Pending'),
    ('R', 'Reject'),
]
class Application(models.Model):

    name = models.CharField(max_length=30)
    details = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    content = models.TextField(max_length=300)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='P')
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return "Application from" + self.name