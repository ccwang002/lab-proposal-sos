from flask import Flask, render_template, request
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, DateTimeField, SubmitField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dont let your boss see this'
bootstrap = Bootstrap(app)


@app.errorhandler(404)
def page_not_found(e):
    path = request.path
    return render_template('404.html', path=path), 404


@app.route('/')
def index():
    '''Lab Project SOS index page.

    TODO:
    - list all project
    - add new project page ``/new``
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
    start_time = DateTimeField('開始執行')
    time_span = StringField('執行期間')
    submit = SubmitField('建立')


@app.route('/new', methods=['GET', 'POST'])
def new_proj():
    '''New project'''
    form = ProjectForm()
    if form.validate_on_submit():
        pass
    return render_template('new_proj.html', form=form)


# run flask
if __name__ == '__main__':
    app.run(debug=True)
