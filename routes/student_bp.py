from flask import Blueprint,redirect,url_for,request,render_template
from controllers.studentController import *
from controllers.steamController import *


student_bp=Blueprint('student_bp',__name__)

@student_bp.route('/')
def home_route():
    ptitle="Dashboard"
    return render_template('dashboard.html',ptitle=ptitle)


@student_bp.route('/students')
def students_route():
    ptitle="Students"
    students=get_students()
    return render_template('students.html',students=students,ptitle=ptitle)

@student_bp.route('/student/<sid>',methods=['GET'])
def student_route(sid):
    student=get_student(sid)
    ptitle="Student Details"
    return render_template('student_details.html',student=student,ptitle=ptitle)


@student_bp.route('/student/add', methods=['GET', 'POST'])
def add_student_route():
    ptitle="Student Add"
    if request.method=='POST':
        firstName=request.form['firstName']
        lastName=request.form['lastName']
        classId=request.form['classId']
        add_student(firstName, lastName, classId)
        return redirect(url_for('student_bp.students_route'))
    streams=get_class_streams()
    return render_template('student_add.html',streams=streams,ptitle=ptitle)


@student_bp.route('/student/edit/<sid>', methods=['GET', 'POST'])
def edit_student_route(sid):
    ptitle="Student Edit"
    student=get_student(sid)
    if request.method=='POST':
        firstName=request.form['firstName']
        lastName=request.form['lastName']
        classId=request.form['classId']
        edit_student(firstName, lastName, classId, sid)
        return redirect(url_for('student_bp.students_route'))
    streams=get_class_streams()
    return render_template('student_edit.html',student=student, streams=streams, ptitle=ptitle)


@student_bp.route('/student/delete/<sid>')
def delete_student_route(sid):
    delete_student(sid)
    return redirect(url_for('student_bp.students_route'))