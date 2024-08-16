from flask import Flask
from routes.stream_bp import stream_bp
from routes.student_bp import student_bp

app=Flask(__name__)
app.register_blueprint(stream_bp)
app.register_blueprint(student_bp)



if __name__ == "__main__":
    app.run(debug=True)