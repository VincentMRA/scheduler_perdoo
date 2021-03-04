from django.test import TestCase
from .models import Req, Resp
from scheduler.my_scheduler import scheduler
import datetime


class ReqTestCase(TestCase):
    def test_scheduler_has_event(self):
        """
        Validate the creation of a request adds a job to the scheduler.
        """
        number_of_events_scheduled = len(scheduler.get_jobs())
        Req.objects.create(
            title="test",
            type="0",
            url="https://api.github.com/repos/stoplightio/prism/stats/contributors",
            exec_date=datetime.datetime.now() + datetime.timedelta(seconds=60),
        )
        self.assertEqual(number_of_events_scheduled + 1, len(scheduler.get_jobs()))


# class RespTestCase(TestCase):
#     def execute_request_creates_response(self):
#         """
#         Validate the excute request generates a response
#         """
#         return
