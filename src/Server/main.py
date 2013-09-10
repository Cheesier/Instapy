from bottle import route, run, request, static_file
from API.Upload import Upload
from API.Filter import Filter
from CImageInstagram import *
from os import path
import json
import Lib
import os
import shutil

APIs = {'upload': Upload(),
        'filter': Filter(),
        }

PUBLIC_PATH = '../../public/'

@route('/upload', method='POST')
def upload():
    data = request.files.data
    filtername = str(request.forms.filter)
    #print "data:", data
    if data and data.file:        
        fn = path.basename(data.filename)
        fileName, fileExtension = os.path.splitext(fn)
        
        open(PUBLIC_PATH + 'tmp/' + fn, 'wb').write(data.file.read())
        hashName = Lib.hashImg(fileName+fileExtension)
        shutil.copyfile(PUBLIC_PATH + 'tmp/' + fn, PUBLIC_PATH + 'tmp/' + hashName+fileExtension)
        #open('../../public/tmp/' + hashName + "." + fileExtension, 'wb').write(data.file.read())
        
        return {'org': '/tmp/'+hashName + fileExtension,
                'available_filters': filter_list.keys(),
                'hash': hashName}
    return {'error':"Did not receive a file"}

@route('/filter')
@route('/filter/<filename>')
@route('/filter/<filename>/<filtername>')
def do_filter(filename="girl.jpg", filtername="blur"):
    return APIs['filter'].process(filename, filtername)

@route('/')
@route('/<filename:path>')
def send_static(filename='index.html'):
    return static_file(filename, root=PUBLIC_PATH)

run(host='0.0.0.0', port=8181, reloader=True, server='paste')