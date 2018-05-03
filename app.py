from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from data import Projects, Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

# Config mySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
# TODO Store password and other parameters into environment variables
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mhccClub'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#initialize MYSQL
mysql = MySQL(app)

Projects = Projects()

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/calendar')
def calendar():
	return render_template('calendar.html')

@app.route('/projects')
def projects():
	return render_template('projects.html', projects = Projects)

@app.route('/project/<string:id>/')
def project(id):
	return render_template('project.html', id=id)

# TODO put this class into a different file
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
        ])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Create cursor
        cur = mysql.connection.cursor()

        # TODO Clean this up line is too long
        # Executes query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Congratulations! You are now registered!', 'success')

        return redirect(url_for('index'))

    return render_template('register.html', form=form)

if __name__ == '__main__':
    # Make the key secure and store in an envrionment variable
    app.secret_key='secret123'
    app.run(debug=True)
