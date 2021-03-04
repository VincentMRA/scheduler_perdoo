from django.contrib import admin
from .models import Req, Resp
from datetime import datetime

# Register your models here.

admin.site.register(Resp)


@admin.register(Req)
class ReqAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "exec_date", "url", "type")

    def status(self, obj):
        if hasattr(obj, "resp"):
            if obj.resp.status == 0:
                return "Failed"
            return obj.resp.status

        else:
            if obj.exec_date.replace(tzinfo=None) < datetime.utcnow():
                return "The scheduler missed the deadline"
            return "No Resp Yet"
