import database
from course_available import Course
from employee import Employee
import sqlite3


class Admin:

    def __init__(self, admin_id, admin_pass, admin_name=None):
        self.user_name = admin_name
        self.user_id = admin_id
        self.user_pass = admin_pass
        self.conn = database.Database.connection()
        self.employee = None
        self.course = Course()
        pass

    def get_employee_details(self):
        emp_name = input("Enter your name ")
        emp_id = input("Enter your ID ")
        emp_pass = input("Enter your password ")
        self.employee = Employee(emp_id, emp_pass, emp_name)

    def admin_register(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO admin VALUES(?,?,?) ", (self.user_id, self.user_name, self.user_pass))
            print("*************Registered successfully************************")
            print("Enter details of Admin are:\nID : {}\nname : {}\npassword : {} ".format(self.user_id, self.user_name,
                                                                                           self.user_pass))
            # db.close()
        except sqlite3.Error:
            print("There is error or may be user has already registered.")
        finally:
            self.conn.commit()
            cursor.close()

    def admin_login(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT id, password FROM admin WHERE id = '{}'".format(self.user_id))
            row = cursor.fetchone()
            if row is not None:
                new_id, password = row
                if self.user_id == new_id and self.user_pass == password:
                    print("You have Logged in successfully")
                    self.more_action_for_admin(True)
                    exit(1)
            else:
                print("Enter ID : {} and password : {} is not valid".format(self.user_id, self.user_pass))
        except sqlite3.Error:
            print("No user available")
        finally:
            self.conn.commit()
            cursor.close()

    def trainee_details(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT emp_id, name FROM Employee")
            rows = cursor.fetchall()
            if rows is not None:
                for row in rows:
                    id, name = row
                    print("Trainee ID : {}\t Name : {}".format(id, name))
        except sqlite3.Error:
            print("No data available")
        finally:
            self.conn.commit()
            cursor.close()

    def more_action_for_admin(self, login):
        if login:
            print("What do you want Now\n\n 1. Add Course\t 2. Have a look on available courses\t 3. Add trainee "
                  "\t 4. Assign course\n\n 5. Have a look on trainee details\t 6.Track_Training_record \t 7.Exit"
                  "\n\n press your choice")
            while True:
                choice = int(input())
                if choice == 1:
                    self.course.add_courses()
                elif choice == 2:
                    self.course.see_available_courses()
                elif choice == 3:
                    self.get_employee_details()
                    self.employee.employee_register()
                elif choice == 4:
                    self.course.assign_course()
                elif choice == 5:
                    self.trainee_details()
                elif choice == 6:
                    self.see_track_record()
                elif choice == 7:
                    break
                else:
                    print("Sorry you have entered wrong choice TRY Again:")
        else:
            print("Sorry you have not logged in!")

    def see_track_record(self):
        cursor = self.conn.cursor()
        try:
            print("Search ... Do you want to see particular record press 1 else press 2\n")
            choice = int(input())
            if choice == 1:
                id_ = input("Enter Trainee ID")
                cursor.execute("SELECT Employee.emp_id, name, course_name, start_date,end_date,status FROM Employee "
                               "JOIN Assign_course ON Employee.emp_id = Assign_course.emp_id WHERE Employee.emp_id = "
                               "'{}'".format(id_))
            else:
                cursor.execute("SELECT Employee.emp_id, name, course_name, start_date,end_date,status FROM Employee "
                               "JOIN Assign_course ON Employee.emp_id = Assign_course.emp_id")
            rows = cursor.fetchall()
            if rows is not None:
                for row in rows:
                    emp_id, name, c_name, s_date, e_date, status = row
                    print(
                        "Trainee_ID : {}\t Name : {}\t Assign_course : {}\t start_date : {}\t end_date : {}\t Status "
                        ":{} ".format(
                            emp_id,
                            name,
                            c_name,
                            s_date,
                            e_date,
                            status))

        except sqlite3.Error:
            print("No Record Found")
        finally:
            cursor.close()
