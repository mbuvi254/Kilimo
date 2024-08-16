from models.streamModel import SteamsModel


steams_model=SteamsModel()

def add_class_stream(className):
    try:
        steams_model.add_class_steam(className)
        return True
    except Exception as e:
        print(f"Error adding class stream: {e}")
        return False
    

def edit_class_stream(className,id):
    try:
        steams_model.edit_class_stream(className, id)
        return True
    except Exception as e:
        print(f"Error editing class stream: {e}")
        return False
    


def get_class_streams():
    try:
        streams=steams_model.get_all_class_streams()
        return streams
    except Exception as e:
        print(f"Error getting all class streams: {e}")
        return []


def get_class_stream(id):
    try:
        stream=steams_model.get_class_steam(id)
        return stream
    except Exception as e:
        print(f"Error getting class stream: {e}")
        return None
    
def delete_class_stream(id):
    try:
        steams_model.delete_class_stream(id)
        return True
    except Exception as e:
        print(f"Error deleting class stream: {e}")
        return False
    

def class_stream_students(id):
    try:
        students=steams_model.get_students_in_class_stream(id)
        return students
    except Exception as e:
        print(f"Error getting students in class stream: {e}")
        return []