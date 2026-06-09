import hashlib
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

IST = ZoneInfo("Asia/Kolkata")


def make_run_id(product_key: str, iso_week: str) -> str:
    """Deterministic run identifier: sha1(product_key + iso_week)."""
    return hashlib.sha1(f"{product_key}{iso_week}".encode()).hexdigest()


def iso_week_to_dates(iso_week: str) -> tuple[date, date]:
    """Return (monday, sunday) for an ISO week string like '2026-W16'."""
    year_str, week_str = iso_week.split("-W")
    year, week = int(year_str), int(week_str)
    monday = date.fromisocalendar(year, week, 1)
    sunday = date.fromisocalendar(year, week, 7)
    return monday, sunday


def current_iso_week(today: date | None = None) -> str:
    """Return the ISO week string for the most recently completed week in IST."""
    if today is None:
        today = datetime.now(IST).date()
    last_week = today - timedelta(weeks=1)
    iso = last_week.isocalendar()
    return f"{iso.year}-W{iso.week:02d}"


def iso_week_label(iso_week: str) -> str:
    """Return a human-readable label like '2026-W16 (Apr 13 → Apr 19)'."""
    monday, sunday = iso_week_to_dates(iso_week)
    return (
        f"{iso_week} "
        f"({monday.strftime('%b')} {monday.day} → "
        f"{sunday.strftime('%b')} {sunday.day})"
    )
