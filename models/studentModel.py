from config.database import Database


class StudentModel:
    def __init__(self):
        self.connection=Database().get_connection()
        self.create_students_table()


    def create_students_table(self):
        try:
            with self.connection.cursor() as cursor:
                create_table="""
                    CREATE TABLE IF NOT EXISTS students (
                        sid INT AUTO_INCREMENT PRIMARY KEY,
                        firstName VARCHAR(255) NOT NULL,
                        lastName VARCHAR(255) NOT NULL,
                        classId VARCHAR(255) NOT NULL,
                        joinDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """
                cursor.execute(create_table)
                self.connection.commit()
                print("Students table created successfully")

        except Exception as e:
            print(f"Error creating students table: {e}")

        
    def add_student(self, firstName, lastName, classId):
        try:
            with self.connection.cursor() as cursor:
                insert_student="INSERT INTO students (firstName, lastName, classId) VALUES (%s, %s, %s)"
                cursor.execute(insert_student, (firstName, lastName, classId))
                self.connection.commit()
                print("Student added successfully")
        except Exception as e:
            print(f"Error adding student: {e}")

    def edit_student(self, firstName, lastName, classId,sid):
        try:
            with self.connection.cursor() as cursor:
                update_student="UPDATE students SET firstName=%s, lastName=%s, classId=%s WHERE sid=%s"
                cursor.execute(update_student, (firstName, lastName, classId, sid))
                self.connection.commit()
                print("Student updated successfully")
        except Exception as e:
            print(f"Error updating student: {e}")

    def get_all_students(self):
        try:
            with self.connection.cursor() as cursor:
                select_students="SELECT * FROM students"
                cursor.execute(select_students)
                result=cursor.fetchall()
                return result
        except Exception as e:
            print(f"Error getting all students: {e}")
    
    def get_student(self, sid):
        try:
            with self.connection.cursor() as cursor:
                select_student="SELECT * FROM students WHERE sid=%s"
                cursor.execute(select_student, (sid,))
                result=cursor.fetchone()
                return result
        except Exception as e:
            print(f"Error getting student: {e}")


    def delete_student(self, sid):
        try:
            with self.connection.cursor() as cursor:
                delete_student="DELETE FROM students WHERE sid=%s"
                cursor.execute(delete_student, (sid,))
                self.connection.commit()
                print(f"Student with id '{sid}' deleted successfully")
        except Exception as e:
            print(f"Error deleting student: {e}")


    def get_class_students(self, sid):
        try:
            with self.connection.cursor() as cursor:
                qry="SELECT * FROM students WHERE classId=%s"
                values=(sid,)
                cursor.execute(qry,values)
                result=cursor.fetchall()
                return result
        except Exception as e:
            print(f"Error getting students in class: {e}")


    def count_class_students(self,sid):
        try:
            with self.connection.cursor() as cursor:
                qry="SELECT COUNT(*) FROM students WHERE classId=%s"
                values=(sid,)
                cursor.execute(qry,values)
                result=cursor.fetchone()
                return result[0]
        except Exception as e:
            print(f"Error counting students in class: {e}")