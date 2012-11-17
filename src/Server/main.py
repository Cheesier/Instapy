from bottle import route, run, request, static_file
from API.Upload import Upload
#from API.Filter import Filter
from os import path

APIs = {'upload': Upload(),
        #'filter': Filter(),
        }

@route('/upload', method='POST')
def upload():
    data = request.files.data
    filter = request.forms.filter
    #print "data:", data
    if data and data.file:
        fn = path.basename(data.filename)
        open('../../public/img/' + fn, 'wb').write(data.file.read())
        
        return 'The file "' + fn + '" was uploaded successfully'
    return "Something went wrong."

@route('/api')
@route('/api/<api>')
@route('/api/<api>/<data>')
def api(api, data=""):
    if api in APIs:
        return APIs[api.lower()].run(data)
    else:
        return "No such API, check documentation."

@route('/')
@route('/<filename:path>')
def send_static(filename='index.html'):
    return static_file(filename, root='../../public')

run(host='127.0.0.1', port=8080, reloader=True)