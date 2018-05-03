from flask import Flask, render_template
from data import Projects, Articles

app = Flask(__name__)

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


if __name__ == '__main__':
	app.run(debug=True)