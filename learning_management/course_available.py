import database
import sqlite3
import math
from datetime import date, timedelta


class Course:

    def __init__(self):
        self.conn = database.Database.connection()

    def add_courses(self):
        course_name = input("Enter name of the course")
        course_duration = input("Enter course duration")
        cursor = self.conn.cursor()
        try:
            # print("Adding.....")
            cursor.execute("INSERT INTO Course VALUES(?,?)", (course_name.upper(), course_duration))
            print("Course added successfully")
        except sqlite3.Error:
            print("Sorry,There is Error in adding the course! May be the course has been already added.")
        finally:
            self.conn.commit()
            cursor.close()

    def assign_course(self):
        trainee_id = input("Enter trainee ID")
        course_name = input("Enter course name")
        cursor = self.conn.cursor()
        # start_date = None
        # end_date = None
        try:
            cursor.execute("SELECT course_duration FROM Course WHERE course_name = '{}'".format(course_name.upper()))
            row = cursor.fetchone()
            cursor.close()
            if row is not None:
                course_time = row[0]
                # course_time = int(input("Enter Course time"))
                day_ = (math.ceil(course_time / 8))
                # print("Days...... {}".format(day_))
                y, m, d = map(int, input("Enter start date of the course as YYYY MM DD").split(' '))
                start_date = date(y, m, d)
                # start_day = datetime.date(y,m,d).strftime("%A")
                ex_ = (math.ceil(day_ / 5)) -1
                # print("Extra..... {}".format(ex_))
                day_ = day_ + (2*ex_) - 1
                end_date = date(y, m, d) + timedelta(days=day_)
                end_day = end_date.strftime("%A")
                if end_day == "Saturday":
                    end_date = date(y, m, d) + timedelta(days=day_ + 2)
                elif end_day == "Sunday":
                    end_date = date(y, m, d) + timedelta(days=day_ + 1)

                if end_date == date.today():
                    status_detail = "Completed today"
                else:
                    status_detail = "In Progress ..."

                print("Start day {}".format(start_date.strftime("%A")))
                print("Expected end day {}".format(end_date.strftime("%A")))
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO Assign_course VALUES(?,?,?,?,?)", (trainee_id, course_name.upper(), start_date, end_date,status_detail))
                print("Course Assign successfully to {} ".format(trainee_id))
        except sqlite3.Error:
            print("No course Available")
        finally:
            self.conn.commit()
            cursor.close()

    def see_available_courses(self):
        cursor = self.conn.cursor()
        try:
            # cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Course")
            for row in cursor.fetchall():
                course_name, duration = row
                print("Course_name : {:<8}\t\t duration : {}".format(course_name, duration))
            self.conn.commit()
            cursor.close()
        except sqlite3.Error:
            print("No courses is available")
        finally:
            self.conn.commit()
            cursor.close()

    def update_available_course(self):
        pass
