from lib.db import create_user, find_user
from lib.stringtools import get_random_string
from .event import publish, EventTypes


def register_new_user(name: str, password: str, email: str):
    # create an entry in the database
    user = create_user(name, password, email)

    # post an event
    publish(EventTypes.REGISTRATION, user)


def password_forgotten(email: str):
    # retrieve the user
    user = find_user(email)

    # generate a password reset code
    user.reset_code = get_random_string(16)

    # post an event
    publish(EventTypes.PASSWORD_CHANGE, user)


def reset_password(code: str, email: str, password: str):

    # retrieve the user
    user = find_user(email)

    # reset the password
    user.reset_password(code, password)


def upgrade_plan(email: str):
    # find the user
    user = find_user(email)

    # upgrade the plan
    user.plan = "paid"

    # post an event
    publish(EventTypes.PLAN_UPGRADE, user)