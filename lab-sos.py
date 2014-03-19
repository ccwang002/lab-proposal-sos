from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    '''Lab Project SOS index page.

    TODO:
    - list all project
    - add new project page ``/new``
    - live search (combine with frontend framework)
    '''
    return '<h1>Lab Project Home</h1>'


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
    return '<h1>Project ID: {}</h1><p>project info here</p>'.format(proj_id)


@app.route('/new')
def new_proj():
    '''New project

    TODO:
    - add new project
    '''
    return '<h1>New Project</h1>'


# run flask
if __name__ == '__main__':
    app.run(debug=True)
