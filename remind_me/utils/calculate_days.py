from calendar import monthrange
from datetime import datetime


def format_date(raw_date):
    formatted_date = datetime.strptime(raw_date, "%d %b %Y")
    return formatted_date


def days_in_month(now=datetime.now()):
    return monthrange(now.year, now.month)[1]
