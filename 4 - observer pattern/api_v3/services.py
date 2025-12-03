
from lib.email import send_email
from lib.log import log
from lib.slack import post_slack_message
from api_v3.event import on_event, EventTypes
from lib.db import User


def register_events() -> None:
    pass


# ── Email ─────────────────────────────────────
@on_event(EventTypes.REGISTRATION)
def _(user: User):
    send_email(user.name, user.email,
        "Welcome",
        f"Thanks for registering, {user.name}!\nRegards, The DevNotes team")

@on_event(EventTypes.PASSWORD_CHANGE)
def _(user: User):
    send_email(user.name, user.email, "Reset your password",
        f"To reset your password, use this very secure code: {user.reset_code}.\nRegards, The DevNotes team")

@on_event(EventTypes.PLAN_UPGRADE)
def _(user: User):
    send_email(user.name, user.email,
        "Thank you",
        f"Thanks for upgrading, {user.name}! You're gonna love it. \nRegards, The DevNotes team")


# ── Log ─────────────────────────────────────
@on_event(EventTypes.REGISTRATION)
def _(user: User):
    log(f"User registered with email address {user.email}")

@on_event(EventTypes.PASSWORD_CHANGE)
def _(user: User):
    log(f"User with email address {user.email} requested a password reset")

@on_event(EventTypes.PLAN_UPGRADE)
def _(user: User):
    log(f"User with email address {user.email} has upgraded their plan")


# ── Slack ─────────────────────────────────────
@on_event(EventTypes.REGISTRATION)
def _(user: User):
    post_slack_message("sales",
        f"{user.name} has registered with email address {user.email}. Please spam this person incessantly.")

@on_event(EventTypes.PLAN_UPGRADE)
def _(user: User):
    post_slack_message("sales",
        f"{user.name} has upgraded their plan.")
