from datetime import datetime
from typing import Tuple
import pytz

TIMEZONE = 'Asia/Ho_Chi_Minh'


def now_in_tz(tz_name: str = TIMEZONE) -> datetime:
    """Return current datetime with the given timezone."""
    return datetime.now(pytz.timezone(tz_name))


def remaining_days_inclusive(target: datetime, now: datetime) -> int:
    """Return number of days remaining (inclusive) between now and target.

    Mirrors the previous behaviour: (target - now).days + 1
    If target is in the past this may be <= 0.
    """
    delta = target - now
    return delta.days + 1


def remaining_dhm(target: datetime, now: datetime) -> Tuple[int, int, int]:
    """Return (days, hours, minutes) remaining until target.

    If target is in the past, returns (0, 0, 0).
    """
    delta = target - now
    total_seconds = int(delta.total_seconds())
    if total_seconds <= 0:
        return (0, 0, 0)

    days = total_seconds // (24 * 3600)
    total_seconds %= (24 * 3600)
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    return (days, hours, minutes)
