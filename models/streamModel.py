from config.database import Database


class SteamsModel:
    def __init__(self):
        self.connection=Database().get_connection()
        self.create_class_steam_table()


    def create_class_steam_table(self):
        try:
            with self.connection.cursor() as cursor:
                create_table="""
                    CREATE TABLE IF NOT EXISTS class_streams (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        className VARCHAR(255)NOT NULL,
                        classDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """
                cursor.execute(create_table)
                self.connection.commit()
                print("Class Stream table created successfully")
        except Exception as e:
            print(f"Error creating class stream table: {e}")


    def add_class_steam(self, className):
        try:
            with self.connection.cursor() as cursor:
                insert_class_steam="INSERT INTO class_streams (className) VALUES (%s)"
                cursor.execute(insert_class_steam, (className,))
                self.connection.commit()
                print(f"Class stream '{className}' added successfully")
        except Exception as e:
            print(f"Error adding class stream: {e}")


    def get_all_class_streams(self):
        try:
            with self.connection.cursor() as cursor:
                select_all_class_streams="SELECT * FROM class_streams"
                cursor.execute(select_all_class_streams)
                result=cursor.fetchall()
                return result
        except Exception as e:
            print(f"Error getting all class streams: {e}")



    def get_class_steam(self,id):
        try:
            with self.connection.cursor() as cursor:
                select_class_steam="SELECT * FROM class_streams WHERE id=%s"
                cursor.execute(select_class_steam, (id,))
                result=cursor.fetchone()
                return result
        except Exception as e:
            print(f"Error getting class stream: {e}")

    def edit_class_stream(self,className,id):
        try:
            with self.connection.cursor() as cursor:
                update_class_steam="UPDATE class_streams SET className=%s WHERE id=%s"
                cursor.execute(update_class_steam, (className, id))
                self.connection.commit()
                print(f"Class stream '{className}' edited successfully")
        except Exception as e:
            print(f"Error editing class stream: {e}")


    def delete_class_stream(self,id):
        try:
            with self.connection.cursor() as cursor:
                delete_class_steam="DELETE FROM class_streams WHERE id=%s"
                cursor.execute(delete_class_steam, (id,))
                self.connection.commit()
                print(f"Class stream with id '{id}' deleted successfully")
        except Exception as e:
            print(f"Error deleting class stream: {e}")



    def get_students_in_class_stream(self, id):
        try:
            with self.connection.cursor() as cursor:
                select_students_in_class_stream="SELECT students.* FROM students JOIN class_streams ON students.classId=class_streams.id WHERE class_streams.id=%s"
                cursor.execute(select_students_in_class_stream, (id,))
                result=cursor.fetchall()
                return result
        except Exception as e:
            print(f"Error getting students in class stream: {e}")




        