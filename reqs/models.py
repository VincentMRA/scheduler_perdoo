from django.db import models
from datetime import datetime
from scheduler.scheduler import add_request


REQTYPES = (("0", "GET"), ("1", "POST"), ("2", "PUT"), ("3", "DELETE"), ("4", "HEAD"))


class Req(models.Model):
    title = models.CharField(max_length=80)
    type = models.CharField(max_length=1, choices=REQTYPES, default="0")
    url = models.URLField()
    exec_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        """
        Adds the request to the scheduler upon saving
        """
        add_request(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Resp(models.Model):
    req = models.OneToOneField(Req, on_delete=models.CASCADE, primary_key=True)
    body = models.JSONField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.req.title + ": " + str(self.status)
