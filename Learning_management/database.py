import sqlite3


class database:

    @staticmethod
    def connection():
        try:
            db = sqlite3.connect('DataBase.sqlite')
            db.execute("CREATE TABLE IF NOT EXISTS admin(id TEXT NOT NULL, name TEXT, password TEXT NOT NULL)")
            db.execute("CREATE TABLE IF NOT EXISTS Employee(emp_id TEXT PRIMARY KEY NOT NULL, name TEXT, emp_pass )")
            db.execute("CREATE TABLE IF NOT EXISTS Course(course_name TEXT PRIMARY KEY NOT NULL,course_duration "
                       "Integer )")
            db.execute("CREATE TABLE IF NOT EXISTS Assign_course(emp_id TEXT NOT NULL,course_name TEXT NOT NULL,"
                       "start_date TEXT, end_date TEXT , status TEXT)")
            return db
        except sqlite3.Error:
            print("There is something wrong in connecting with database")



