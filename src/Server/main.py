from bottle import route, run, request, static_file
from API.Upload import Upload
from API.Filter import Filter
from CImageInstagram import *
from os import path
import json

APIs = {'upload': Upload(),
        'filter': Filter(),
        }

@route('/upload', method='POST')
def upload():
    data = request.files.data
    filtername = str(request.forms.filter)
    #print "data:", data
    if data and data.file:
        fn = path.basename(data.filename)
        open('../../public/tmp/' + fn, 'wb').write(data.file.read())
        
        return {'org': 'http://localhost:8080/tmp/'+fn,
                'filtered': do_filter(fn, filtername),
                'available_filters': filter_list.keys()}
    return "Something went wrong"


@route('/filter')
@route('/filter/<filename>')
@route('/filter/<filename>/<filtername>')
def do_filter(filename="girl.jpg", filtername="blur"):
    return APIs['filter'].process(filename, filtername)

@route('/')
@route('/<filename:path>')
def send_static(filename='index.html'):
    return static_file(filename, root='../../public')

run(host='127.0.0.1', port=8080, reloader=True, debug=True, server='paste')