from flask import Flask, render_template
app = Flask(__name__)

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


@app.route('/new')
def new_proj():
    '''New project

    TODO:
    - add new project
    '''
    return render_template('new_proj.html')


# run flask
if __name__ == '__main__':
    app.run(debug=True)
