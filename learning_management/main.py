from admin import Admin
from employee import Employee


def get_admin_details():
    while True:
        try:
            choice = int(input("press 1 to register \t and 2 to sign in\n"))
            return choice
        except ValueError:
            print("Invalid choice please try again")


def get_trainee_details():
    while True:
        try:
            choice = int(input("press 1 to login \t and 2 to exit\n"))
            return choice
        except ValueError:
            print("Invalid choice please try again")


def get_choice():
    while True:
        try:
            choice = int(input("If you are admin : \npress 1 \nIf you are trainee :\npress 2\n"))
            return choice
        except ValueError:
            print("Invalid choice please try again")


if __name__ == '__main__':
    while True:
        user_choice = get_choice()
        if user_choice == 1:
            admin_choice = get_admin_details()
            if admin_choice == 1:
                user_name = input("Enter your name Admin \n")
                user_id = input("Enter your ID Admin \n")
                user_pass = input("Enter your password Admin \n")
                admin = Admin(user_id, user_pass, user_name)
                admin.admin_register()
            elif admin_choice == 2:
                user_id = input("Enter your ID Admin")
                user_pass = input("Enter your password")
                admin = Admin(user_id, user_pass)
                admin.admin_login()
            else:
                print("Sorry you have entered wrong option! please Try again.")
        elif user_choice == 2:
            trainee_choice = get_trainee_details()
            if trainee_choice == 1:
                user_id = input("Enter your ID ")
                user_pass = input("Enter your password")
                trainee = Employee(user_id, user_pass)
                trainee.employee_login()
            elif trainee_choice == 2:
                exit(1)
            else:
                print("Sorry you have entered wrong option! please Try Again.")
        else:
            print("Sorry you have entered wrong option! please Try Again.")
