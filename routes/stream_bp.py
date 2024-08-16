from flask import Blueprint,render_template,request,redirect,url_for

from controllers.steamController import *
from controllers.studentController import *

stream_bp=Blueprint('stream_bp',__name__)


@stream_bp.route('/class/streams')
def class_streams_route():
    ptitle="Class Streams"
    streams=get_class_streams()
    return render_template('class_streams.html',ptitle=ptitle,streams=streams)


@stream_bp.route('/class/stream/add', methods=['GET', 'POST'])
def add_class_stream_route():
    if request.method=='POST':
        className=request.form['className']
        if add_class_stream(className):
            return redirect(url_for('stream_bp.class_streams_route'))
    ptitle="Add Class Stream"
    return render_template('add_class_stream.html',ptitle=ptitle)


@stream_bp.route('/class/stream/edit/<id>', methods=['GET', 'POST'])
def edit_class_stream_route(id):
    if request.method=='POST':
        className=request.form['className']
        if edit_class_stream(className, id):
            return redirect(url_for('stream_bp.class_streams_route'))
    ptitle="Edit Class Stream"
    stream=get_class_stream(id)
    return render_template('edit_class_stream.html',ptitle=ptitle,stream=stream)


@stream_bp.route('/class/stream/delete/<id>')
def delete_class_stream_route(id):
    delete_class_stream(id)
    return redirect(url_for('stream_bp.class_streams_route'))


@stream_bp.route('/class/stream/<sid>' ,methods=['GET'])
def class_stream_route(sid):
    ptitle="Class Stream Details"
    stream=get_class_stream(sid)
    students=get_class_students(sid)
    studentCount=student_class_count(sid)
    return render_template('class_stream_details.html',ptitle=ptitle,stream=stream,students=students,studentCount=studentCount)