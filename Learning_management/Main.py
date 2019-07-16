import Admin
import Employee


def get_choice():
    while True:
        try:
            choice = int(input("Admin :\t New user ?\t press 1 to Register \t 2 to sign in.\n\nTrainee :\t press 3 to "
                               "sign in \t press 4 to Exit \n"))
            return choice
        except ValueError:
            print("Invalid choice please try again")


if __name__ == '__main__':
    while True:
        user_choice = get_choice()
        if user_choice == 1:
            user_name = input("Enter your name Admin")
            user_id = input("Enter your ID Admin")
            user_pass = input("Enter your password Admin")
            admin = Admin.Admin(user_id,user_pass,user_name)
            admin.admin_register()
        elif user_choice == 2:
            user_id = input("Enter your ID Admin")
            user_pass = input("Enter your password")
            admin = Admin.Admin(user_id, user_pass)
            admin.admin_login()
            break
        elif user_choice == 3:
            user_id = input("Enter your ID ")
            user_pass = input("Enter your password")
            trainee = Employee.Employee(user_id,user_pass)
            trainee.employee_login()
        elif user_choice == 4:
            exit(1)
        else:
            print("Sorry you have entered wrong option! please Try Again.")
