from bottle import route, run, request, static_file
from Filters.CFilterBlur import CFilterBlur
from Filters.CFilterPrime import CFilterPrime
from Filters.CFilterVignette import CFilterVignette
from API.Upload import Upload
from API.Filter import Filter
from CImageInstagram import *
from os import path

APIs = {'upload': Upload(),
        'filter': Filter(),
        }

@route('/upload', method='POST')
def upload():
    data = request.files.data
    filtername = request.forms.filter
    #print "data:", data
    if data and data.file:
        fn = path.basename(data.filename)
        open('../../public/tmp/' + fn, 'wb').write(data.file.read())
        
        return {'org': 'http://localhost:8080/tmp/'+fn,
                'filtered': api("filter", filtername)}
    return "Something went wrong"

@route('/api')
@route('/api/<api>')
@route('/api/<api>/<data>')
def api(api, data):
    if api in APIs:
        return APIs[api.lower()].run(data)
    else:
        return "No such API, check documentation."

@route('/')
@route('/<filename:path>')
def send_static(filename='index.html'):
    return static_file(filename, root='../../public')

run(host='127.0.0.1', port=8080, reloader=True, debug=True)