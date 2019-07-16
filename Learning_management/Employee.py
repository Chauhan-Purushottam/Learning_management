import database
import sqlite3
import Course_available


class Employee():

    def __init__(self, user_id, password, name=None):
        self.user_name = name
        self.user_id = user_id
        self.user_pass = password
        self.conn = database.database.connection()
        self.isLogin = False
        self.course = Course_available.course()

    def employee_register(self):
        cursor = self.conn.cursor()
        try:
            # cursor = self.conn.cursor()
            cursor.execute("INSERT INTO Employee VALUES(?,?,?) ", (self.user_id, self.user_name, self.user_pass))
            print("*************Registered successfully************************")
            # self.conn.commit()
            # cursor.close()
        except sqlite3.Error:
            print("Sorry there is something wrong Please Try again")
        finally:
            self.conn.commit()
            cursor.close()

        print("Enter details of Current Trainee is :\nID : {}\nname : {}\npassword : {} ".format(self.user_id,
                                                                                                 self.user_name,
                                                                                                 self.user_pass))

    def employee_login(self):
        print("Enter ID : {} and password : {}".format(self.user_id, self.user_pass))
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT emp_id, emp_pass FROM Employee WHERE emp_id ='{}'".format(self.user_id))
            row = cursor.fetchone()
            if row is not None:
                id, password = row
                if self.user_id == id and self.user_pass == password:
                    self.isLogin = True
                    print("You have Logged in successfully")
                    self.more_to_explore()
            else:
                print("User Id and password are not valid!")
        except sqlite3.Error:
            print("No Trainee with this ID")
        finally:
            self.conn.commit()
            cursor.close()

    def more_to_explore(self):
        if self.isLogin:
            print("\nHow can we help you ?\n\n 1. See Profile\t 2. Update profile\t 3.See training program "
                  "\n\n 4. comment status\t 5. See Available courses \t 6.Exit"
                  "\n\n press your choice")
            while True:
                choice = int(input())
                if choice == 1:
                    self.employee_details()
                elif choice == 2:
                    self.update_record()
                elif choice == 3:
                    self.see_training_plan()
                elif choice == 4:
                    self.comment_status()
                elif choice == 5:
                    self.available_course()
                elif choice == 6:
                    break
                else:
                    print("Sorry you have entered wrong choice TRY Again:")
        else:
            print("Sorry you have not logged in.Please log in")

    def employee_details(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT emp_id, name FROM Employee WHERE emp_id = '{}'".format(self.user_id))
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

    def see_training_plan(self):
        cursor = self.conn.cursor()
        try:
            print("Search ... Do you want to see your record press 1 else press 2\n")
            choice = int(input())
            if choice == 1:
                cursor.execute("SELECT Employee.emp_id, name, course_name, start_date,end_date,status FROM Employee "
                               "JOIN Assign_course ON Employee.emp_id = Assign_course.emp_id WHERE Employee.emp_id = "
                               "'{}'".format(self.user_id))
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

    def update_record(self):
        cursor = self.conn.cursor()
        try:
            print("Do you want to change your password")
            user_pass = input("Enter your current password \n")
            cursor.execute("SELECT emp_id FROM Employee WHERE emp_pass = '{}'".format(user_pass))
            row = cursor.fetchone()
            if row is not None:
                self.user_pass = input("Enter new password")
                cursor.execute(
                    "UPDATE Employee SET emp_pass = '{}' WHERE emp_id = '{}'".format(self.user_pass, self.user_id))
                print("Password Updated successfully......")
            else:
                print("Invalid user_id - password")
        except sqlite3.Error:
            print("*******************No user available***********************")
        finally:
            self.conn.commit()
            cursor.close()

    def comment_status(self):
        cursor = self.conn.cursor()
        try:
            print("Do you have to update training status ? press 1")
            choice = int(input())
            if choice == 1:
                status = input("Enter current status\n")
                cursor.execute(
                    "UPDATE Assign_course SET status = '{}' WHERE emp_id = '{}'".format(status, self.user_id))
                print("You have successfully updated your training status........")
        except sqlite3.Error:
            print("Sorry ! There is some Error your status has not updated yet.")
        finally:
            self.conn.commit()
            cursor.close()

    def available_course(self):
        self.course.see_available_courses()
