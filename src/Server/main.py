from bottle import route, run, template, request, static_file, error
from API.Upload import Upload

APIs = {'upload': Upload()}

@route('/upload', method='POST')
def upload():
    data = request.files.data
    #print "data:", data
    if data and data.file:
        raw = data.file.read() # This is dangerous for big files
        filename = data.filename
        return "Hello! You uploaded %s (%d bytes)." % (filename, len(raw))
    return "Something went wrong."

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

run(host='127.0.0.1', port=8080, reloader=True)