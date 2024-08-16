from models.studentModel import StudentModel

student_model=StudentModel()

def get_students():
    students=student_model.get_all_students()
    return students


def get_student(sid):
    student=student_model.get_student(sid)
    return student


def add_student(firstName, lastName, classId):
    student_model.add_student(firstName, lastName, classId)



def edit_student(firstName, lastName, classId, sid):
    student_model.edit_student(firstName, lastName, classId, sid)


def delete_student(sid):
    student_model.delete_student(sid)

def get_class_students(sid):
    students=student_model.get_class_students(sid)
    return students

def student_class_count(sid):
    studentCount=student_model.count_class_students(sid)
    return studentCount