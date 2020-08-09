#from logic import *
from portalvars import *
from flask import render_template, request, redirect, url_for
from app import app
from werkzeug.security import generate_password_hash, check_password_hash
import json


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('start.html', title='Home')
    elif request.method == 'POST':
        userType = request.form['type']
        if (userType == "teacher"):
            return redirect(url_for('teacherLogin'))
        elif (userType == "student"):
            return redirect(url_for('studentLogin'))


@app.route('/teacherLogin', methods=['GET', 'POST'])
def teacherLogin():
    if request.method == 'GET':
        return render_template('teacherLogin.html', title='Teacher')
    elif request.method == 'POST':
        userName = request.form.get('username')
        pwd = request.form.get('pass')
        if len(list(db[teacherCollection].find({"username":userName}))) != 0:
            hashPwd = list(db[teacherCollection].find({"username":userName}))[0]['password']
            if check_password_hash(hashPwd,pwd):
                return redirect(url_for('teacherHome'))
            else:
                return "Password did not match"
        else:
            return "No such user"

@app.route('/studentLogin', methods=['GET', 'POST'])
def studentLogin():
    if request.method == 'GET':
        return render_template('studentLogin.html', title='Student')
    elif request.method == 'POST':
        userName = request.form.get('username')
        pwd = request.form.get('pass')
        if len(list(db[studentCollection].find({"username":userName}))) != 0:
            hashPwd = list(db[studentCollection].find({"username":userName}))[0]['password']
            if check_password_hash(hashPwd,pwd):
                return redirect(url_for('studentHome'))
            else:
                return "Password did not match"
        else:
            return "No such user"

@app.route('/admin', methods=['GET', 'POST'])
def adminLogin():
    if request.method == 'GET':
        return render_template('adminLogin.html', title='Student')
    elif request.method == 'POST':
        userName = request.form.get('username')
        pwd = request.form.get('pass')
        if len(list(db[adminCollection].find({"adminName":userName}))) != 0:
            hashPwd = list(db[adminCollection].find({"adminName":userName}))[0]['adminPassword']
            if check_password_hash(hashPwd,pwd):
                return redirect(url_for('adminHome'))
            else:
                return "Password did not match"
        else:
            return "No such user"

@app.route('/adminHome', methods=['GET', 'POST'])
def adminHome():
    if request.method == 'GET':
        return render_template('adminHome.html', title='AdminHome')

@app.route('/createTeacher', methods=['GET', 'POST'])
def createTeacher():
    if request.method == 'GET':
        return render_template('createTeacher.html', title='Create Teacher')
    elif request.method == 'POST':
        teacherName = request.form.get('name')
        teacherUserName = request.form.get('username')
        teacherPassword = request.form.get('password')
        teacherPhone = request.form.get('phone')
        teacherSubject =[ json.loads(sub.replace("\'", "\"")) for sub in request.form.getlist('subject') ]
        db[teacherCollection].insert({"name":teacherName,
                                      "username": teacherUserName,
                                      "password":generate_password_hash(teacherPassword),
                                      "phone" : teacherPhone,
                                      "subject" : teacherSubject })
        print(teacherName + "\n" + teacherUserName + "\n" + teacherPassword + "\n" + teacherPhone + "\n" + str(teacherSubject))
        return "added"

@app.route('/createStudent', methods=['GET', 'POST'])
def createStudent():
    if request.method == 'GET':
        return render_template('createStudent.html', title='Create Student')
    elif request.method == 'POST':
        studentName = request.form.get('name')
        studentUserName = request.form.get('username')
        studentPassword = request.form.get('password')
        studentPhone = request.form.get('phone')
        studentClass = request.form.get('class')
        studentSection = request.form.get('section')
        print(request.form)
        #studentSubject =[ json.loads(sub.replace("\'", "\"")) for sub in request.form.getlist('subject') ]
        db[studentCollection].insert({"name":studentName,
                                      "username": studentUserName,
                                      "password":generate_password_hash(studentPassword),
                                      "phone" : studentPhone,
                                      "class" : studentClass,
                                      "section" : studentSection
                                      })
        print(studentName + "\n" + studentUserName + "\n" + studentPassword + "\n" + studentPhone + "\n" )
        return "added"

@app.route('/teacherHome',methods=['GET','POST'])
def teacherHome():
    if request.method == 'GET':
        return render_template('teacherHome.html', title='Teacher Home')

@app.route('/questions',methods=['GET','POST'])
def questions():
    if request.method == 'GET':
        return render_template('trial.html', title='questions')

@app.route('/createTest',methods=['GET','POST'])
def createTest():
    if request.method == 'GET':
        return render_template('createTest.html', title='Create Test')