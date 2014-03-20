from flask import Flask, render_template, request, flash, redirect, url_for
from flask.ext.script import Manager

from flask.ext.bootstrap import Bootstrap

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

import os
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dont let your boss see this'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
)
bootstrap = Bootstrap(app)
manager = Manager(app)
db = SQLAlchemy(app)


class Project(db.Model):
    __tablename__ = 'projs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(256), index=True)
    mod_time = db.Column(db.Unicode(128))
    start_time = db.Column(db.Unicode(128), nullable=True)
    time_span = db.Column(db.Unicode(128), nullable=True)

    def __repr__(self):
        return '<Project {}>'.format(self.title)

@app.errorhandler(404)
def page_not_found(e):
    path = request.path
    return render_template('404.html', path=path), 404

@app.route('/')
def index():
    '''Lab Project SOS index page.

    TODO:
    - list all project
    - live search (combine with frontend framework)
    '''
    return render_template('index.html')


@app.route('/proj/<proj_id>')
def proj_page(proj_id):
    '''Project page

    TODO:
    - show project information
    - modify project info  ``/proj/<id>/edit``
    - upload file
    - modify file
    - delete file
    '''
    return render_template('proj_page.html', proj_id=proj_id)


class ProjectForm(Form):
    title = StringField('標題', validators=[Required()])
    start_time = StringField('開始執行')
    time_span = StringField('執行期間')
    submit = SubmitField('建立')


@app.route('/new', methods=['GET', 'POST'])
def new_proj():
    '''New project'''
    form = ProjectForm()
    if form.validate_on_submit():
        flash('New Project has been created.', category='new-proj')
        return redirect(url_for('index'))
    return render_template('new_proj.html', form=form)


# run flask
if __name__ == '__main__':
    manager.run()
