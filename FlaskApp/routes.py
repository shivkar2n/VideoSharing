import os
from flask import (request, render_template, redirect, url_for, abort, flash)
from .models import User, Video, Comment,db
from . import app, login_manager
from flask_login import login_required, login_user, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime

ALLOWED_EXTENSIONS = {'mp4','avi','ogg'}

def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def Home():
    Videos = Video.query.all()
    if current_user.is_authenticated:
        if request.method == 'POST':
            C = Comment(Content=request.form["VideoComment"],Commenter_id=current_user.id,Video_id=request.form["VideoId"])
            db.session.add(C)
            db.session.commit()
            return redirect(url_for('Home'))
    return render_template('Home.html',Videos=Videos)

@app.route('/login', methods=['GET','POST'])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':
        for U in User.query.all():
            if request.form["Username"] == U.Username and check_password_hash(U.Password,request.form["Password"]):
                login_user(U)
                flash("Login successful!!")
                return redirect(url_for('Home'))

        flash("Password or username incorrect!")
        return redirect(url_for('Login'))

    return render_template('Login.html')

@app.route('/register', methods=['GET','POST'])
def Register():
    if current_user.is_authenticated:
        return redirect(url_for('Home'))

    if request.method == 'POST':
        for U in User.query.all():
            if U.Username == request.form["Username"]:
                flash("Username already taken")
                return redirect(url_for('Register'))

        U = User(Username=request.form["Username"],Password=generate_password_hash(request.form["Password"]),Description=request.form["Description"],Location=request.form["Location"])
        db.session.add(U)
        db.session.commit()
        flash("Successfully registered! You can login now!")
        return redirect(url_for('Home'))
    return render_template('Register.html')

@app.route('/upload', methods=['GET','POST'])
def Upload():
    if current_user.is_authenticated:
        if request.method == 'POST':
            file = request.files['Video']
            if file.filename == '':
                flash('No selected file')
                return redirect(url_for('Upload'))

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.root_path,'static/video', filename))

                V = Video(Title=request.form["Title"],FileName=filename,Uploader_id=current_user.id)
                db.session.add(V)
                db.session.commit()

                flash("Video Successfully Uploaded!")
                return redirect(url_for('Home'))
        return render_template('Upload.html')

    else:
        flash("To upload you need to be logged in!")
        return redirect(url_for('Home'))

@app.route('/myprofile')
@login_required
def MyProfile():
    if current_user.is_authenticated:
        U = User.query.filter_by(id=current_user.id).first()
        Videos =Video.query.all()
        return render_template('MyProfile.html',User=U,Videos=Videos )
    else:
        return redirect(url_for('home'))

@app.route('/logout')
def Logout():
    if current_user.is_authenticated:
        logout_user()
        flash('You logged out!')
        return redirect(url_for('Home'))
    else:
        return redirect(url_for('Home'))
