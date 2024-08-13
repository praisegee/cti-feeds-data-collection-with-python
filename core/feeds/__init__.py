from .commercial.xforce import XForce
from .open_source.abuse_ch import AbuseCH
from utils.notification import Email


def fetch_feeds():
    # x = XForce().save_to_db()
    count = AbuseCH().save_to_db()
    stats = f"Abuse.ch: {count} data retrieved."
    Email().send(stats)
