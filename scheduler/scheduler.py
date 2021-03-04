from .my_scheduler import scheduler
from datetime import datetime, timedelta
import logging
import requests

logger = logging.getLogger(__name__)

if not scheduler.running:
    scheduler.start()


def add_request(req):
    """
    Adds a request to the scheduler
    """
    try:
        scheduler.add_job(execute_request, "date", run_date=req.exec_date, args=[req])
    except Exception as e:
        logger.error("Add Request error: ", e)


def execute_request(req):
    from reqs.models import Resp

    try:
        url = req.url
        if req.type == "0":
            r = requests.get(url)
        elif req.type == "1":
            r = requests.post(url)
        elif req.type == "2":
            r = requests.put(url)
        elif req.type == "3":
            r = requests.delete(url)
        elif req.type == "4":
            r = requests.head(url)
        body = r.text
        status = r.status_code
        resp = Resp(body=body, status=status, req=req)
        resp.save()
    except Exception as e:
        logger.error("Bad Request: ", e)
        resp = Resp(body={"ERROR": "BAD REQUEST"}, status=0, req=req)
        resp.save()
