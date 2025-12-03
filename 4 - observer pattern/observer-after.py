from api_v3.user import register_new_user, password_forgotten, upgrade_plan
from api_v3 import services 


services.register_events()


# example endpoints
def user_create() -> None:
    register_new_user("Arjan", "BestPasswordEva", "hi@arjanegges.com")

def user_password_forget() -> None:
    password_forgotten("hi@arjanegges.com")

def user_plan_upgrade() -> None:
    upgrade_plan("hi@arjanegges.com")


def main() -> None:
    user_create()
    user_password_forget()
    user_plan_upgrade()


if __name__ == "__main__":
    main()
    

