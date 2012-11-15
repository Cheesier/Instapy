from bottle import route, run, template, request, static_file, error
from API.Upload import Upload

APIs = {'upload': Upload()}

@route('/upload', method='POST')
def upload():
    name = request.forms.name
    data = request.files.data
    if name and data and data.file:
        raw = data.file.read() # This is dangerous for big files
        filename = data.filename
        return "Hello %s! You uploaded %s (%d bytes)." % (name, filename, len(raw))
    return "You missed a field."

@route('/api/<api>')
def test(api):
    if api in APIs:
        return APIs[api.lower()].run("")
    else:
        return "No such API, check documentation"

@route('/')
@route('/<filename:path>')
def send_static(filename='index.html'):
    return static_file(filename, root='../../public')

run(host='localhost', port=8080, reloader=True)